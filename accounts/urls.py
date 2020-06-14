from django.urls import path
from.import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('projects', views.projects, name='projects'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]
