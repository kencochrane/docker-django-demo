from dockerdemo.celery import app
from .models import Choice, Vote


@app.task(ignore_result=True)
def register_vote(choice_pk, ip_address):
    """A little overkill, but a good example of a task
    that can be done in the background"""
    try:
        selected_choice = Choice.objects.get(pk=choice_pk)
    except (KeyError, Choice.DoesNotExist):
        # no reason to continue
        return
    else:
        vote = Vote()
        vote.selection = selected_choice
        vote.ip_address = ip_address
        vote.save()
