import os
import sys

sys.path.append('/home/kenney/Projects')

os.environ['DJANGO_SETTINGS_MODULE'] = 'AYMCommonMessage.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

