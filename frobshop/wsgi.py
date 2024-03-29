"""
WSGI config for frobshop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append("/var/django/frobshop")
sys.path.append("/var/django/frobshop/frobshop")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "frobshop.settings")
from dj_static import Cling

from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()
application = Cling(get_wsgi_application())
