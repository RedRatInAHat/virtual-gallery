from django.urls import path
from . import views

urlpatterns = [path('gallery', views.index, {'pagename': 'gallery'}, name='home'),
               path('gallery/<str:year>/', views.get_year_info, name='year')]
