from __future__ import unicode_literals

import datetime

from voting.models import Vote
from django.utils import timezone
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Delete any votes older than 2 days"

    def handle(self, **options):
        cutoff_date = timezone.now() - datetime.timedelta(days=2)
        Vote.objects.filter(vote_date__lt=cutoff_date).delete()
