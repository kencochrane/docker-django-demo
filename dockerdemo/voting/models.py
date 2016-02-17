from __future__ import unicode_literals
import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    last_update = models.DateTimeField('last updated', auto_now=True)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)

    @property
    def votes(self):
        """How many votes does this choice have."""
        return self.vote_set.count()

    def __str__(self):
        return self.choice_text


class Vote(models.Model):
    vote_date = models.DateTimeField('date voted', auto_now=True)
    selection = models.ForeignKey(Choice, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()

    def old_vote(self):
        """Votes older then 2 days are old"""
        return self.vote_date <= timezone.now() - datetime.timedelta(days=2)

    def __str__(self):
        return "{}:{}".format(self.ip_address, self.selection)
