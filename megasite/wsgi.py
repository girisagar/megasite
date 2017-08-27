#! /home/pi/Envs/megasite/bin/python2.7
"""
WSGI config for megasite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import sys

sys.path.append('/var/www/sgiri.com')

#
#from django.core.wsgi import get_wsgi_application
#from mezzanine.utils.conf import real_project_name
#
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "megasite.settings" )
#
#application = get_wsgi_application()

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application()
application = DjangoWhiteNoise(application)

