from django.shortcuts import render, redirect
from .models import Topic, AboutTopic
from .forms import TopicForm, AboutTopicForm, EntryForm

# Create your views here.
def index(request):
    # Home page for progress log app
    return render(request, 'progress_log/index.html')

def topics(request):
    # Showing all topics
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'progress_log/topics.html', context)

def about_topic(request, topic_id):
    about_topic = AboutTopic.objects.order_by('date_added')
    topic = Topic.objects.get(id=topic_id)
    descriptions = []

    for description in about_topic:     # Did this because about_topic IDs for its topic does not match topic's ID
        if str(description.topic) == topic.text:
            descriptions.append(description)

    context = {'topic': topic, 'about_topic': descriptions}
    return render(request, 'progress_log/about_topic.html', context)

def topic(request, topic_id):
    # Shows specific topic and its entries based on its ID
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')   # Minus sign for reverse order (most recent shows up first)
    context = {'topic': topic, 'entries': entries}
    return render(request, 'progress_log/topic.html', context)

def new_topic(request):
    # Allows user to create new topics
    if request.method != 'POST':
        form = TopicForm()  # Creates blank form since no data submitted
    else:
        # POST and process data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('progress_log:topics')

    # Displays a blank or invalid form
    context = {'form':form}
    return  render(request,'progress_log/new_topic.html',context)

def new_about_topic(request, topic_id):
    # Adding new about topic section for topic
    topic = Topic.objects.get(id=topic_id)

    if request.method != "POST":
        form = AboutTopicForm()
    else:
        form = AboutTopicForm(data=request.POST)
        if form.is_valid():
            new_about_topic = form.save(commit=False)
            new_about_topic.topic = topic
            new_about_topic.save()
            return redirect('progress_log:about_topic',topic_id=topic_id)
    # Displays a blank/invalid form
    context = {'form': form,'topic': topic}
    return render(request,'progress_log/new_about_topic.html', context)

def new_entry(request, topic_id):
    # Adding new entry for topic
    topic = Topic.objects.get(id=topic_id)

    if request.method != "POST":
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('progress_log:topic',topic_id=topic_id)
    # Displays a blank/invalid form
    context = {'form': form,'topic':topic}
    return render(request,'progress_log/new_entry.html', context)


