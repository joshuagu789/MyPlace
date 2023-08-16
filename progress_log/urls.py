from django.urls import path
from . import views

app_name = 'progress_log'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics
    path('topics/', views.topics, name='topics'),
    # Page that shows entries of specific topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Home page of topic
    path('topics/<int:topic_id>/about/', views.about_topic, name='about_topic'),
    # Page to create new topics
    path('new_topic/', views.new_topic, name='new_topic'),
]