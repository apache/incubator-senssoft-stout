"""
WSGI config for xdata project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os, sys
sys.path.append('/var/www/op_task/xdata')
sys.path.append('/var/www/op_task')

sys.path.append('./xdata/settings')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "production")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
