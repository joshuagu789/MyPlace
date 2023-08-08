from django.shortcuts import render
from .models import Topic, AboutTopic

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
    #about_topic = AboutTopic.objects.get(id=topic_id)
    about_topic = AboutTopic.objects.order_by('date_added')
    topic = Topic.objects.get(id=topic_id)
    context = {'topic': topic, 'about_topic': about_topic}
    return render(request, 'progress_log/about_topic.html', context)

def topic(request, topic_id):
    # Shows specific topic and its entries based on its ID
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')   # Minus sign for reverse order (most recent shows up first)
    context = {'topic': topic, 'entries': entries}
    return render(request, 'progress_log/topic.html', context)