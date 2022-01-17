from django.shortcuts import render, redirect, reverse
import requests
from django.conf import settings
from django.contrib.auth.models import User
from .models import List, Result
import os
from .forms import CreateList
from slugify import slugify


mapbox_key = os.environ.get('MAPBOX_KEY', '')
skywatch_key = os.environ.get('SKYWATCH_KEY', '')

# display the homepage
def homepage(request):
    return render(request, 'index.html')

# save the form
def save(request):

    form = CreateList(request.POST)

    # if the form is valid, save it
    if form.is_valid():
        #form.save(commit=False)
        print("is valid")
    
    # if it's not valid, return to form
    else:

        print(form)
       
        context = {
            'form': form,
            'validation': 'Form not valid',
        }

        return render(request, 'create_pipeline.html', context)

    return render(request, 'save.html')

# create a pipeline
def create(request):

    # current logged in user
    user = str(request.user)

    # if user posts the form
    if request.method == 'POST':

        # fill in form details with users values
        form = CreateList(request.POST)

        # if form is valid, save as object and call the pipeline
        # fill in other fields of object
        # redirect to detail view of object
        if form.is_valid():
           
            # put aoi into correct format
            format_aoi = form.cleaned_data['aoi']['features'][0]['geometry']

            # api url
            url = 'https://api.skywatch.co/earthcache/pipelines'

            # api parameters required
            params = {
                'name': form.cleaned_data['pipeline_name'],
                'interval': form.cleaned_data['interval'],
                'start_date': str(form.cleaned_data['start_date']),
                'output': {
                    'id': form.cleaned_data['output_image'],
                    'format': 'geotiff',
                    'mosaic': 'off'
                },
                'end_date': str(form.cleaned_data['end_date']),
                'aoi': format_aoi,
                'max_cost': 0,
                'min_aoi_coverage_percentage': 50,
                'result_delivery': {
                    'max_latency': '0d',
                    'priorities': [
                        'latest',
                        'highest_resolution',
                        'lowest_cost'
                    ]
                },
                'resolution_low': 30,
                'resolution_high': 10,
                'tags': []
            }

            print(params)

            # post the pipeline to the api
            try:
                post_pipeline = requests.post(
                    url,
                    headers={'x-api-key': skywatch_key},
                    json=params)
                post_response = post_pipeline.json()

                print(post_response)

            # don't use bare except
            except:
                print("Couldn't reach API")
                # redirect to page saying api could not be found

            # if the api returns errors in returning a response,
            # redirect to form page with error message
            # (should not happen due to form validation, Django + JS)
            if 'errors' in post_response or 'error' in post_response:

                form = CreateList(request.POST)
                # error message

                context = {
                    'form': form,
                    # error message
                }

            # if no errors in api response,
            # save form as object and fill in other fields
            else:

                form.save()

                # get the object id
                current_list = List.objects.latest('id')

                api_id = post_response['data']['id']
                #current_list.slug = slugify(pipeline_name)
                current_list.created_by = user
                current_list.status = 'pending'
                current_list.api_id = api_id
                current_list.save()
                
        # if form is not valid
        # return to form
        else:
            print('NOT VALID')

    form = CreateList()

    context = {
        'form': form,
    }

    return render(request, 'create_pipeline.html', context)