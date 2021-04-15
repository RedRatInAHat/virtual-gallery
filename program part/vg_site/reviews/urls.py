from django.urls import path
from . import views

urlpatterns = [path('reviews', views.review_main, {'pagename': 'reviews'}, name='home'), ]
