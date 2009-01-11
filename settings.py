import os, datetime
ROOT_PATH = os.path.dirname(__file__)

# setting up directory paths
TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH,'templates'),
    os.path.join(ROOT_PATH,'pages')
)
STATIC_DIR = os.path.join(ROOT_PATH,'static')
DEPLOY_DIR = os.path.join(ROOT_PATH,'deploy')
IMAGES_DIR = os.path.join(ROOT_PATH,'images')
TMP_DIR = os.path.join(ROOT_PATH, 'aym_tmp_files')
PAGES_DIR = os.path.join(ROOT_PATH, 'pages')

# path for YUICompressor, or None if you don't
# want to compress JS/CSS. Project homepage:
# http://developer.yahoo.com/yui/compressor/
#YUI_COMPRESSOR = "./yuicompressor-2.4.1.jar"
YUI_COMPRESSOR = None # if you don't want to use YUI compressor

# path for HSS, which is a preprocessor for CSS-like files (*.hss)
# project page at http://ncannasse.fr/projects/hss
HSS_PATH = "./hss-1.0-osx"
#HSS_PATH = None # if you don't want to use HSS


# Set true if you want to use CleverCSS with all .css files.
# Must be installed via "sudo easy_install CleverCSS" before
# usage.
# USE_CLEVER_CSS = True
USE_CLEVER_CSS = True
CLEVER_CSS_EXT = ".ccss"

# setting up some helpful values
STATIC_URL_FORMAT = u"/static/%s"
STATIC_THUMBNAIL_FORMAT = STATIC_URL_FORMAT % u"thumbnail/%s"
STATIC_IMAGE_FORMAT = STATIC_URL_FORMAT % u"image/%s"
THUMBNAIL_SIZE = (128,128)
EMAIL = u"lakshmi.vyas@gmail.com"

# creating default rendering context
CONTEXT = {
    'email':EMAIL,
    'now':datetime.datetime.now(),
    'badge_selectors': {"badge_new": "#javascript" },
    'products': [{'name': 'Shelved', 'disabled': True, 'image': "Shelved_128x128.png"},
                 {'name': 'Goalce', 'disabled': False, 'image': "what2do.png"}, 
                 {'name': 'Unknown1', 'disabled':True, 'image': "blank.png"}, 
                 {'name': 'Unknown2', 'disabled':True, 'image': "blank.png"}],
    'code_categories': [{'name': 'Python', 'disabled': True},
                        {'name': 'Javascript', 'disabled': False},
                        {'name': 'Cocoa', 'disabled': True}]
}

PAGES_TO_RENDER = (
    u"index.html",
)

INSTALLED_APPS = (
    'aym_tags',
    'django.contrib.webdesign'
)
