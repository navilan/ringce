import os

ROOT_PATH = os.path.dirname(__file__)

#Directories
SITE_TEMPLATE_DIR = os.path.join(ROOT_PATH, 'templates')
CONTENT_DIR = os.path.join(ROOT_PATH, 'content')
MEDIA_DIR = os.path.join(ROOT_PATH, 'media')
DEPLOY_DIR = os.path.join(ROOT_PATH, 'deploy')
TMP_DIR = os.path.join(ROOT_PATH, 'deploy_tmp')
BACKUPS_DIR = os.path.join(ROOT_PATH, 'backups')


# {folder : extension : (processors)}
# The processors are run in the given order and are chained.
# Only a lone * is supported for folders. Path shoud be specifed 
# starting under the media folder. For example, if you have media/css under 
# your site root,you should specify just css. If you have media/css/ie you 
# should specify css/ie for the folder name. css/* is not supported (yet).

# Extensions do not support wildcards.
GENERATE_ABSOLUTE_FS_URLS = True

MEDIA_PROCESSORS = {
	'*':{
		'.css':('hyde.processors.TemplateProcessor','hyde.processors.YUICompressor',),
		'.ccss':('hyde.processors.TemplateProcessor','hyde.processors.CleverCSS', 'hyde.processors.YUICompressor',),
		'.hss':('hyde.processors.TemplateProcessor','hyde.processors.HSS', 'hyde.processors.YUICompressor',),

	} 
}

CONTEXT = {
    'content':CONTENT_DIR,
	'groups':("Products", "Open Source", "Blog", "About"),
	'badge_selectors': {"badge_new": "#javascript"},
	'products': (
		{'name': 'Shelved', 'disabled': True, 'image': "Shelved_128x128.png"},
		{'name': 'Goalce', 'disabled': False, 'image': "what2do.png"},             
		{'name': 'Hyde', 'disabled':False, 'image': "hyde-icon.png"},                
		{'name': 'Unknown2', 'disabled':True, 'image': "blank.png"}),   
	'code_categories': (
		{'name': 'Python', 'disabled': True},
		{'name': 'Javascript', 'disabled': False},                       
		{'name': 'Cocoa', 'disabled': True}
	),
	'all_links': {
		"jQuery v1.2.6" : "http://jquery.com/",
		"jQuery UI v1.6RC4" : "http://ui.jquery.com/",
		"jQuery Form Plugin v2.18": "http://malsup.com/jquery/form/",
		"MIT": "http://www.opensource.org/licenses/mit-license.php",
		"GPL": "http://www.gnu.org/copyleft/gpl.html"
	}
	
}

#Processor Configuration

# path for YUICompressor, or None if you don't
# want to compress JS/CSS. Project homepage:
# http://developer.yahoo.com/yui/compressor/
YUI_COMPRESSOR = "../hyde/tools/yuicompressor-2.4.1.jar"
#YUI_COMPRESSOR = None 

# path for HSS, which is a preprocessor for CSS-like files (*.hss)
# project page at http://ncannasse.fr/projects/hss
HSS_PATH = "../hyde/tools/hss-1.0-osx"
#HSS_PATH = None # if you don't want to use HSS

#Django settings

TEMPLATE_DIRS = ( SITE_TEMPLATE_DIR, CONTENT_DIR, MEDIA_DIR, TMP_DIR )

INSTALLED_APPS = (
	'hyde',
    'django.contrib.webdesign'
)


