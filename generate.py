import os, shutil, commands
from django.template.loader import render_to_string
from django.conf import settings
from PIL import Image

os.environ['DJANGO_SETTINGS_MODULE'] = u"settings"

def main():
	# retrieving default context dictionary from settings
	context = settings.CONTEXT
	deploy_dir = settings.DEPLOY_DIR
	tmp_dir = settings.TMP_DIR

	print u"Removing existing deploy dir, if any..."
	shutil.rmtree(deploy_dir,ignore_errors=True)
	print u"Removing existing temp dir, if any.."
	shutil.rmtree(tmp_dir,ignore_errors=True)
	
	print u"Creating deploy/ dir..."
	os.mkdir(deploy_dir)
	
	print u"Creating temp directory at '%s'" % tmp_dir
	os.mkdir(tmp_dir)
	
	print u"Copying contents of static/ into deploy/static..."
	(static_dir_path,static_dir_name) = os.path.split(settings.STATIC_DIR)
	deploy_static_dir = os.path.join(deploy_dir, static_dir_name)
	process_static_dir(settings.STATIC_DIR)
	create_thumbnails(os.path.join(tmp_dir, os.path.basename(settings.STATIC_DIR)), context)
	render_pages(tmp_dir, context)
	

def filter_unwanted(item_list):
	if(not len(item_list)): return
	wanted = filter(lambda item: not (item.startswith('.') or item.endswith('~')), item_list)
	count = len(item_list)
	good_item_count = len(wanted)
	if(count == good_item_count): return
	item_list[:good_item_count] = wanted
	for i in range(good_item_count, count):
		item_list.pop()

def get_path_fragment(root_dir, dir):
	current_dir = dir
	current_fragment = ''
	while (not os.path.samefile(current_dir, root_dir)):
		(current_dir, current_fragment_part) = os.path.split(current_dir)
		current_fragment = os.path.join(current_fragment_part, current_fragment)
	return current_dir

def mirror_dir_tree(directory, source_root, mirror_root):
	current_fragment = get_path_fragment(source_root, directory)
	mirror_directory = os.path.join(mirror_root, os.path.basename(source_root), current_fragment)
	try:
		os.makedirs(mirror_directory)
	except:
		pass
	return mirror_directory
	
def process_static_dir(static_dir):
	for root, dirs, files in os.walk(static_dir):
		filter_unwanted(dirs)
		filter_unwanted(files)
		tmp_static_dir = mirror_dir_tree(root, settings.STATIC_DIR, settings.TMP_DIR)
		for file in files:
			process_static_file(root, file, tmp_static_dir)
			
def process_static_file(static_dir, static_file, output_dir):
	(file_name, extension) = os.path.splitext(static_file)
	compress = settings.YUI_COMPRESSOR
	hss = settings.HSS_PATH
	ccss = settings.USE_CLEVER_CSS
	
	processed_file_path = os.path.join(output_dir, static_file)
	commands.getoutput(u"cp %s %s" % (os.path.join(static_dir, static_file), processed_file_path))
	if(hss and extension == ".hss"):
		processed_file_path = convert_hss(hss, processed_file_path, remove_source=True)
	
	if(ccss and extension == ".ccss"):
		processed_file_path = convert_ccss(processed_file_path, remove_source=True)
		
	(file_name, extension) = os.path.splitext(processed_file_path)
	
	if(compress and (extension == ".js" or extension == ".css")):
		processed_file_path = compress_file(compress, processed_file_path, processed_file_path)
		
def convert_hss(hss, file, remove_source):
	print u"Compiling HSS[%s] to CSS" % file
	(file_name, extension) = os.path.splitext(file)
	out_file = file_name + ".css"
	s,o = commands.getstatusoutput(u"%s %s -output %s/" % (hss, file, os.path.dirname(out_file)))
	if s > 0: print o
	if(remove_source):
		os.remove(file)
	return out_file
	
def convert_ccss(file, remove_source):
	print u"Compiling CCSS[%s] to CSS" % file
	import clevercss
	(file_name, extension) = os.path.splitext(file)
	out_file = file_name + ".css"
	fin = open(file, 'r')
	data = fin.read()
	fin.close()
	fout = open(out_file,'w')
	fout.write(clevercss.convert(data))
	fout.close()
	if(remove_source):
		os.remove(file)
	return out_file

def compress_file(compress, file, out_file):
	print u"Compressing %s" % file
	tmp_file = file + ".z-tmp-"
	s,o = commands.getstatusoutput(u"java -jar %s %s > %s" % (compress, file, tmp_file))
	if s > 0: 
		print o
	else:
		commands.getoutput(u"mv %s %s" % (tmp_file, out_file))
	return out_file
	
def create_thumbnails(deploy_static_dir, context):
	print u"Copying and creating thumbnails for files in images/..."
	deploy_thumb_path = os.path.join(deploy_static_dir,'thumbnail')
	deploy_image_path = os.path.join(deploy_static_dir,'image')
	os.mkdir(deploy_thumb_path)
	os.mkdir(deploy_image_path)

	images = []
	images_dict = {}
	images_dir = settings.IMAGES_DIR
	thumb_format = settings.STATIC_THUMBNAIL_FORMAT
	image_format = settings.STATIC_IMAGE_FORMAT
	thumbnail_dimensions = settings.THUMBNAIL_SIZE
	
	for filename in os.listdir(images_dir):
		# only process if ends with image file extension
		before_ext,ext = os.path.splitext(filename)
		if ext not in (".png",".jpg",".jpeg"):
			continue

		print u"Copying and thumbnailing %s..." % filename
		filepath = os.path.join(images_dir,filename)
		im = Image.open(filepath)
		im.save(os.path.join(deploy_image_path, filename),ext[1:].upper())
		im.thumbnail(thumbnail_dimensions, Image.ANTIALIAS)
		im.save(os.path.join(deploy_thumb_path, filename), ext[1:].upper())

		# create dict with image data 
		image_dict = {}
		image_dict['filename'] = filename
		image_dict['thumbnail'] = thumb_format % filename
		image_dict['image'] = image_format % filename

		images.append(image_dict)
		# before_ext is 'hello' in 'hello.png'
		images_dict[before_ext] = image_dict

	context['images'] = images
	context['images_dict'] = images_dict
	
def render_pages(out_dir, context):
	print u"Rendering pages..."
	for root, dirs, files in os.walk(settings.PAGES_DIR):
		filter_unwanted(dirs)
		filter_unwanted(files)
		for page in files:
			print u"Rendering %s..." % page
			rendered = render_to_string(page, context)
			source_dir = os.path.dirname(page)
			page_out_dir = mirror_dir_tree(source_dir, settings.PAGES_DIR, out_dir)
			page_path = os.path.join(page_out_dir,page)
			fout = open(page_path,'w')
			fout.write(rendered)
			fout.close()

if __name__ == "__main__":
   main()
