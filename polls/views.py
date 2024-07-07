
# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Poll, Vote
from .forms import VoteForm

def poll_detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    if request.method == 'POST':
        form = VoteForm(poll, request.POST)
        if form.is_valid():
            choice = form.cleaned_data['choice']
            Vote.objects.update_or_create(user=request.user, poll=poll, defaults={'choice': choice})
            choice.votes += 1
            choice.save()
            return redirect('polls:poll_results', poll_id=poll.id)
    else:
        form = VoteForm(poll)

    return render(request, 'polls/poll_detail.html', {'poll': poll, 'form': form})

def poll_results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/poll_results.html', {'poll': poll})
