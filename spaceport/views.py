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

# save the form
def save(request):

    form = CreateList()
    
    # if the form is valid, save it
    if form.is_valid():
        #form.save()
        print("is valid")
    
    # if it's not valid, return to form
    else:
       
        context = {
            'form': form,
            'validation': 'Form not valid',
        }
        return render(request, 'create_pipeline.html', context)

    return render(request, 'save.html')

# create a pipeline
def create(request):

    form = CreateList()

    context = {
        'form': form,
    }

    return render(request, 'create_pipeline.html', context)