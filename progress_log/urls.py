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
    # Page to add new about topic sections
    path('new_about_topic/<int:topic_id>/', views.new_about_topic, name='new_about_topic'),
    # Page to add new entries
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
]