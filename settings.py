import os

ROOT_PATH = os.path.dirname(__file__)

#Directories
LAYOUT_DIR = os.path.join(ROOT_PATH, 'layout')
CONTENT_DIR = os.path.join(ROOT_PATH, 'content')
MEDIA_DIR = os.path.join(ROOT_PATH, 'media')
DEPLOY_DIR = os.path.join(ROOT_PATH, 'deploy')
TMP_DIR = os.path.join(ROOT_PATH, 'deploy_tmp')
BACKUPS_DIR = os.path.join(ROOT_PATH, 'backups')
SITEMAP_FILE = os.path.join(TMP_DIR, 'sitemap.xml')
SITEMAP_GENERATOR = os.path.join(ROOT_PATH, 
 "../hyde/lib/sitemap_gen-1.4/sitemap_gen.py")

BACKUP = False

SITE_WWW_URL = "http://www.ringce.com"
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
GENERATE_ABSOLUTE_FS_URLS = False

MEDIA_PROCESSORS = {
    '*':{ 
        '.css':( 
                'hydeengine.media_processors.TemplateProcessor',
                'hydeengine.media_processors.YUICompressor',),
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

SITE_POST_PROCESSORS = {
    '/' : {
        'hydeengine.site_post_processors.GoogleSitemapGenerator' : {
            'sitemap_file':SITEMAP_FILE,
            'generator': SITEMAP_GENERATOR,
            
        }
    },
    'media/js/': {
        'hydeengine.site_post_processors.FolderFlattener' : {
                'remove_processed_folders': True,
                'pattern':"*.js"
        }
    }
}

GIT_HUB = "http://github.com/lakshmivyas"
TED = "http://www.ted.com/index.php/talks"

CONTEXT = {
    'content':CONTENT_DIR,
    'groups':("Products", "Open Source", "Blog", "About"),
    'badge_selectors': {"badge-new": "#jquery"},
    'products': (
        {'name': 'Shelved', 'disabled': True, 'image': "Shelved_128x128.png"},
        {'name': 'Goalce', 'disabled': False, 'image': "what2do.png"},
        {'name': 'Hyde', 'disabled':False, 'image': "hyde-icon.png"},
        {'name': 'Unknown2', 'disabled':True, 'image': "blank.png"}),
    'code_categories': (
        {'name': 'Python', 'disabled': True},
        {'name': 'jQuery', 'disabled': False},
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
        "Hyde": {
            "Download": GIT_HUB + "/hyde/zipball/master",
            "Source": GIT_HUB + "/hyde",
            "Forum": "http://groups.google.com/group/hyde-dev"},
        "Ringce": {
            "Download": GIT_HUB + "/ringce/zipball/master",
            "Source": GIT_HUB + "/ringce"},
        "jquery-inplace-modal": {
            "Download": GIT_HUB + "/jquery-ui-inplace-modal/zipball/master",
            "Source": GIT_HUB + "/jquery-ui-inplace-modal"},
        "jquery-badge": {
            "Download": GIT_HUB + "/jquery-ui-badge/zipball/master",
            "Source": GIT_HUB + "/jquery-ui-badge"},
        "jquery-ajax-machine": {
            "Download": GIT_HUB + "/jquery-ui-ajax-machine/zipball/master",
            "Source": GIT_HUB + "/jquery-ui-ajax-machine"},
        "Tamil": "http://en.wikipedia.org/wiki/Tamil",
        "5RingsBook": "http://en.wikipedia.org/wiki/Book_of_five_rings",
        "Mushashi": "http://en.wikipedia.org/wiki/Miyamoto_Musashi",
        "NatureTedTalk": TED + "/janine_benyus_shares_nature_s_designs.html",
        "ProjectPlus": "http://github.com/ciaran/projectplus/tree/master",
        "JavascriptLint":"http://www.javascriptlint.com/",
        "PyChecker": "http://svn.textmate.org/trunk/Bundles/Python.tmbundle",
        "CSSEdit":"http://macrabbit.com/cssedit/",
        "Xylescope": "http://culturedcode.com/xyle/",
        "Webkit": "http://webkit.org/",
        "Firebug": "https://addons.mozilla.org/en-US/firefox/addon/1843",
        "IPython":"http://ipython.scipy.org/moin/",
        "Textmate":"http://macromates.com/",
        "Markdown":"http://daringfireball.net/projects/markdown/",
        "Twitter":"http://twitter.com/lakshmivyas",
        "Facebook":"http://www.facebook.com/people/Lakshmi-Vyasarajan/614146002",
        "FriendFeed":"http://friendfeed.com/lakshmivyas",
        "LinkedIn":"http://www.linkedin.com/in/lakshmivyas",
        "Delicious":"http://delicious.com/ezlux",
        "Flickr":"http://www.flickr.com/photos/ezlux",
        "GitHub":GIT_HUB,
        "Ohloh":"http://www.ohloh.net/accounts/lakshmivyas",
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

TEMPLATE_DIRS = (LAYOUT_DIR, CONTENT_DIR, TMP_DIR)

INSTALLED_APPS = (
    'hydeengine',
    'django.contrib.webdesign',
)


