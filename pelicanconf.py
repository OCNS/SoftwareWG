#!/usr/bin/env python
# -*- coding: utf-8 -*- #


AUTHOR = 'INCF/OCNS members'
SITENAME = 'INCF/OCNS Software WG'
TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'
USE_FOLDER_AS_CATEGORY = False
LOAD_CONTENT_CACHE = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_PAGES_ON_MENU = False
INDEX_SAVE_AS = 'blog_index.html'

# Blogroll
LINKS = (
    ('Home', '/index.html'),
    ('Updates', '/blog_index.html'),
    ('Members', '/pages/members.html'),
    ('Contact', '/pages/contact.html'),
    ('INCF', 'https://www.incf.org/'),
    ('OCNS', 'https://www.cnsorg.org/'),
)


# Social widget
ICONS = (
    ('fas fa-comments', 'https://github.com/OCNS/SoftwareWG/discussions/12'),
    ('fab fa-github', 'https://github.com/OCNS/SoftwareWG'),
    ('fab fa-twitter', 'https://twitter.com/INCForg/'),
    ('fab fa-twitter', 'https://twitter.com/CNSorg/'),
    ('fas fa-rss', '/feeds/all.atom.xml'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
ARTICLE_PATHS = ['']
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'

ARCHIVES_SAVE_AS = 'pages/archives.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

STATIC_PATHS = [
    'images',
    'extras'
]

EXTRA_PATH_METADATA = {
    'extras/yeti-bootstrap.min.css': {'path': 'theme/css/bootstrap.min.css'},
}


# Theme
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['assets']

THEME = 'themes/pelican-alchemy/alchemy'
BOOTSTRAP_CSS = '/theme/css/bootstrap.min.css'

SITESUBTITLE = "The OCNS/INCF Software Working Group"
DESCRIPTION = "The OCNS/INCF Software Working GrouP"

FILENAME_METADATA = ''

TYPOGRIFY = True
