#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://ocns.github.io/SoftwareWG/'

FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/categories/{slug}.atom.xml'
CATEGORY_FEED_RSS = 'feeds/categories/{slug}.rss.xml'
TAG_FEED_ATOM = 'feeds/tags/{slug}.atom.xml'
TAG_FEED_RSS = 'feeds/tags/{slug}.rss.xml'
AUTHOR_FEED_ATOM = 'feeds/authors/{slug}.atom.xml'
AUTHOR_FEED_RSS = 'feeds/authors/{slug}.rss.xml'
FEED_MAX_ITEMS = 10

DELETE_OUTPUT_DIRECTORY = False

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
