#-*- coding:utf-8 -*-
import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'BLOG.settings'

path = os.path.dirname(os.path.abspath(__file__)) + '/BLOG'
if path not in sys.path:
    sys.path.insert(1, path)

from django.core.handlers.wsgi import WSGIHandler
from bae.core.wsgi import WSGIApplication

application = WSGIApplication(WSGIHandler())



deps_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], 'deps')
sys.path.insert(0, deps_path)
