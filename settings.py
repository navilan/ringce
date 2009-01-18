import os

ROOT_PATH = os.path.dirname(__file__)

#Directories
LAYOUT_DIR = os.path.join(ROOT_PATH, 'layout')
CONTENT_DIR = os.path.join(ROOT_PATH, 'content')
MEDIA_DIR = os.path.join(ROOT_PATH, 'media')
DEPLOY_DIR = os.path.join(ROOT_PATH, 'deploy')
TMP_DIR = os.path.join(ROOT_PATH, 'deploy_tmp')
BACKUPS_DIR = os.path.join(ROOT_PATH, 'backups')

SITE_NAME = "Ringce"
DATETIME_FORMAT = "%Y-%m-%d %H:%M"

# {folder : extension : (processors)}
# The processors are run in the given order and are chained.
# Only a lone * is supported as an indicator for folders. Path 
# shoud be specifed. No wildcard card support yet.
 
# Starting under the media folder. For example, if you have media/css under 
# your site root,you should specify just css. If you have media/css/ie you 
# should specify css/ie for the folder name. css/* is not supported (yet).

# Extensions do not support wildcards.
GENERATE_ABSOLUTE_FS_URLS = True

MEDIA_PROCESSORS = {
    '*':{
        '.css':('hydeengine.media_processors.TemplateProcessor','hydeengine.media_processors.YUICompressor',),
    } 
}

CONTENT_PROCESSORS = {
    '*': {
        '.html':('hydeengine.content_processors.YAMLContentProcessor',
                # If you want to create a dictionary in python instead:
                # 'hydeengine.content_processors.PyContentProcessor'
                # Needs py.code.
        )
    }
}

CONTEXT = {
    'content':CONTENT_DIR,
    'groups':("Products", "Open Source", "Blog", "About"),
    'badge_selectors': {"badge-new": "#javascript"},
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
    'links': {
        "WillLarson": "http://lethain.com/",
        "aym_cms": "http://aymcms.com/",
        "Django":"http://www.djangoproject.com/",
        "Liquid": "http://www.liquidmarkup.org/",
        "Jekyll": "http://github.com/mojombo/jekyll/tree/master",
        "jQuery v1.2.6" : "http://jquery.com/",
        "jQuery UI v1.6RC4" : "http://ui.jquery.com/",
        "jQuery Form Plugin v2.18": "http://malsup.com/jquery/form/",
        "MIT": "http://www.opensource.org/licenses/mit-license.php",
        "GPL": "http://www.gnu.org/copyleft/gpl.html",
        "HydeSource": "http://github.com/lakshmivyas/hyde",
        "HydeDownload": "http://github.com/lakshmivyas/hyde",
    }
    
}

#Processor Configuration

# path for YUICompressor, or None if you don't
# want to compress JS/CSS. Project homepage:
# http://developer.yahoo.com/yui/compressor/
YUI_COMPRESSOR = "../hyde/lib/yuicompressor-2.4.1.jar"
#YUI_COMPRESSOR = None 

# path for HSS, which is a preprocessor for CSS-like files (*.hss)
# project page at http://ncannasse.fr/projects/hss
#HSS_PATH = "../hyde/lib/hss-1.0-osx"
HSS_PATH = None # if you don't want to use HSS

#Django settings

TEMPLATE_DIRS = ( LAYOUT_DIR, CONTENT_DIR, TMP_DIR)

INSTALLED_APPS = (
    'hydeengine',
    'django.contrib.webdesign',
)


