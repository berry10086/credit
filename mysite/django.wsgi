import os
import sys

path = '/home/br/'
sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'


import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()