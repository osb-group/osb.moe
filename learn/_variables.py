from sphinx.websupport import WebSupport
import os

# This file is just meant for storing constants and stuff.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE_DIR = os.path.join(BASE_DIR, 'docs/osb-learn/')
BUILD_DIR = os.path.join(BASE_DIR, 'docs/osb-learn/_build')
STATIC_DIR = os.path.join(BASE_DIR, 'static/docs/')

support = WebSupport(srcdir=SOURCE_DIR,
                     builddir=BUILD_DIR,
                     search='null',
                     staticdir=STATIC_DIR)