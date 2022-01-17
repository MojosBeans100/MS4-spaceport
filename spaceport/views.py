from django.shortcuts import render, redirect, reverse
import requests
from django.conf import settings
from django.contrib.auth.models import User
import os
from .forms import CreateList


mapbox_key = os.environ.get('MAPBOX_KEY', '')
skywatch_key = os.environ.get('SKYWATCH_KEY', '')

# display the homepage
def homepage(request):
    return render(request, 'index.html')

# create a pipeline
def create(request):

    form = CreateList()

    context = {
        'form': form,
    }

    return render(request, 'create_pipeline.html', context)