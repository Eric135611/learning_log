from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# define the function
def check_topic_owner(request, topic):
    if topic.owner != request.user:
        raise Http404


# Create your views here.

def index(request):
    '''the main page'''
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    '''show all topics'''
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    '''show the topic and its all entries'''
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(request, topic)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """add new topic"""
    if request.method != 'POST':
        # not provide data: create a blank form
        form = TopicForm()
    else:
        #POST have provide the data: deal with the data
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
        
    context = {'form': form}
    return render(request,'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """add new entry in specific topic"""
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(request, topic)
    
    if request.method != 'POST':
        # not provide data: create a blank form
        form = EntryForm()
    else:
        #POST provide the data: deal with the data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic_id]))
        
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """edit the exist entries."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(request, topic)

    if request.method != 'POST':
        # when you request the page firstly, it'll use this entry fill the form.
        form = EntryForm(instance=entry)
    else:
        # when POST have provide the data, it'll deal with the data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic.id]))
        
    context = {'topic': topic, 'entry': entry, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)


@login_required
def edit_topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(request, topic)

    if request.method != 'POST':
        form = TopicForm(instance=topic)
    else:
        form = TopicForm(data=request.POST, instance=topic)
        if form.is_valid():
            form.save()
            return redirect(reverse('learning_logs:topics'))
        
    context = {'form': form, 'topic': topic}
    return render(request, 'learning_logs/edit_topic.html', context)