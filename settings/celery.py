"""
App Celery Configuration
"""
###
# Libraries
###
import os

from celery.schedules import crontab
from django.conf import settings
from celery.utils.log import get_task_logger
from celery import Celery
from django.core.management import call_command

logger = get_task_logger(__name__)

###
# Main Configuration
###
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')

app = Celery('settings')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


###
# Crons
###
@app.on_after_configure.connect
def payout_bookings(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute=1, hour=0, day=0),
        payout_billings.s(),
        name="Pay the amount on stripe",
        queue=settings.CELERY_DEFAULT_QUEUE,
    )

@app.task()
def payout_billings():
    call_command('pay_amount')