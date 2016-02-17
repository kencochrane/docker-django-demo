from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Choice, Question, Vote
from .util import get_client_ip
from .tasks import register_vote


class IndexView(generic.ListView):
    template_name = 'voting/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'voting/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'voting/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'voting/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # register vote in the background using celery.
        register_vote.delay(selected_choice.pk, get_client_ip(request))

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('voting:results', args=(question.id,)))
