#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import bulrush


AUTHOR = 'INCF/OCNS members'
SITENAME = 'INCF/OCNS Software WG'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('INCF website', 'https://www.incf.org/'),
         ('Follow INCF on Twitter', 'https://twitter.com/INCForg/'),
         ('OCNS website', 'https://www.cnsorg.org/'),
         ('Follow OCNS on Twitter', 'https://twitter.com/CNSorg/'),
         )

# Social widget
SOCIAL = (('GitHub', 'https://github.com/OCNS/SoftwareWG'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Theme
# https://github.com/textbook/bulrush/tree/19b2fc4d79e7c060218172ae5484a4a216b40921
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['assets']

THEME = bulrush.PATH
JINJA_ENVIRONMENT = bulrush.ENVIRONMENT
JINJA_FILTERS = bulrush.FILTERS

GITHUB_URL = "https://github.com/OCNS/SoftwareWG"

SITESUBTITLE = "The OCNS/INCF Software Working Group"
TWITTER_USERNAME = "INCForg"
BULRUSH_SHOW_SUMMARY = "True"
LICENSE = "CC BY-SA 4.0"
