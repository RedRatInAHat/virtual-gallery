from django.urls import path
from . import views

urlpatterns = [path('gallery', views.index, {'pagename': 'gallery'}, name='home'), ]