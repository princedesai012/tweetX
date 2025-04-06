# from django.conf import settings 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.tweetX_list, name = 'tweet_list'),
    path('create/', views.tweet_create, name = 'tweet_create'),
    path('<int:tweet_id>/edit/', views.tweetX_edits, name = 'tweet_edit'),
    path('<int:tweet_id>/delete/', views.tweetX_delete, name = 'tweet_delete'),    
    path('register/', views.register, name = 'register'),   
    path('tweetX/search/', views.tweet_search, name='tweet_search'),
      
]