'''define the URL's mode of learning_logs '''
from django.urls import path
from . import views

app_name = 'learning_logs'


urlpatterns = [
    #home page
    path('', views.index, name='index'),
    
    #show all topics
    path('topics/', views.topics, name='topics'),

    #the detail page of specific topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    #the page of adding new topic
    path('new_topic/', views.new_topic, name='new_topic'),

    #the page of adding new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # the page of editting topic
    path('edit_topic/<int:topic_id>/', views.edit_topic, name='edit_topic'),

    # the page of editting  entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]