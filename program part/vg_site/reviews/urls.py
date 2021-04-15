from django.urls import path
from . import views

urlpatterns = [path('reviews', views.review_main, {'pagename': 'reviews'}, name='home'),
               path('reviews/read', views.review_read, {'pagename': 'reviews', 'mode': 'read'}, name='read'), ]
