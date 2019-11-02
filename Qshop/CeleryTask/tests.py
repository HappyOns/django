from __future__ import absolute_import
from django.test import TestCase

# Create your tests here.

import smtplib
from email.mime.text import MIMEText
from Qshop.celery import app

@app.task
def add(x,y):
    return x+y
