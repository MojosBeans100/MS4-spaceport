from django.shortcuts import render, redirect, reverse
import requests
from django.conf import settings
from django.contrib.auth.models import User
import os


mapbox_key = os.environ.get('MAPBOX_KEY', '')
skywatch_key = os.environ.get('SKYWATCH_KEY', '')

# display the homepage
def homepage(request):
    return render(request, 'index.html')

# create a pipeline
def create(request):
    return render(request, 'create_pipeline.html')