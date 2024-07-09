from __future__ import absolute_import, unicode_literals

import logging
import os

from celery import shared_task, Celery
from django.conf import settings

from selenium.webdriver.common.by import By

from only_fans_stat.models import Links, AccountDetail
from selenium import webdriver

from configurations import importer

# Load Django configurations
importer.install()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')


# driver = webdriver.Chrome()

logger = logging.getLogger(__name__)

app = Celery("core", broker=settings.CELERY_BROKER_URL)

app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()
