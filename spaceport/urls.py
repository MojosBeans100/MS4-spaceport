from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('create_pipeline.html', views.create, name='create'),
]