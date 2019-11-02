"""
WSGI config for Qshop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Qshop.settings')

application = get_wsgi_application()



"RUUR"
n=[[10,5],[1,6],[6,10],[3,0],[0,3],[0,10],[6,2]]
n.sort()
print(n)
x=7856
y=9033