from django.shortcuts import render, redirect, reverse
import requests
from django.conf import settings
import os


mapbox_key = os.environ.get('MAPBOX_KEY', '')
skywatch_key = os.environ.get('SKYWATCH_KEY', '')

# display the homepage
def homepage(request):

    context = {
        'mapbox': mapbox_key,
        'skywatch': skywatch_key
    }

    return render(request, 'index.html', context)