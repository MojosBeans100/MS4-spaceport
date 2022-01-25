from django.shortcuts import render, redirect, reverse
import requests
from django.conf import settings
from django.contrib.auth.models import User
from .models import List, Result
import os
from .forms import CreateList, UpdateList
from slugify import slugify
import datetime
from django.utils import timezone
import pytz


mapbox_key = os.environ.get('MAPBOX_KEY', '')
skywatch_key = os.environ.get('SKYWATCH_KEY', '')


def homepage(request):
    """
    A view to display the homepage of the website
    Args:
        request (object): HTTP request object.
    Returns:
        Render of homepage
    """

    return render(request, 'index.html')


def discover(request):
    """
    A view to display the discover page of the website
    Website application, context of satellite imagery.
    Args:
        request (object): HTTP request object.
    Returns:
        Render of discover page
    """
    return render(request, 'discover.html')


def api_error(request):
    """
    A view to display the API error page, for any views
    which required callingt the Skywatch API but it is not
    available.

    Args:
        request (object): HTTP request object.
    Returns:
        Render of api error page
    """

    return render(request, 'api_error.html')


def edit(request, id):
    """
    A view to display a short form with pipeline parameters
    which can be updated.  If edited parameters are valid,
    update the model with new values.
    This view does not call the API as none of the updated
    parameters affect the API parameters.

    Args:
        request (object): HTTP request object.
        id: pipeline instance
    Returns:
        Redirect to detailed view of pipeline instance
    """

    edit_time = timezone.now()

    # get the object to update
    this_pipeline = List.objects.get(id=id)
    this_pipeline.time_edited = edit_time
    this_pipeline.save()

    # fill in the form with that object
    form = UpdateList(instance=this_pipeline)

    # if the form has been submitted
    if request.method == 'POST':

        # get user's new values
        form = UpdateList(request.POST, instance=this_pipeline)

        # if the inputs are valid, save the updated object
        if form.is_valid():

            form.save()
            # reach pipeline and update it

        # else

        return redirect(reverse('detail_view', args=[id]))

    context = {
        'form': form,
        'pipeline': this_pipeline,
    }

    return render(request, 'edit_pipeline.html', context)


def save(request):

    form = CreateList(request.POST)

    # if the form is valid, save it
    if form.is_valid():
        
        print("is valid")

    # if it's not valid, return to form
    else:

        context = {
            'form': form,
            'validation': 'Form not valid',
        }

        return render(request, 'create_pipeline.html', context)

    

    return render(request, 'save.html')


def create(request):
    """
    A view to submit the user's form to the API 
    and if valid, save the pipeline/List object.

    Parameters:
    Request - user's submitted form.

    Returns:
    Saved List object
    Redirects to Detail View of List object.
    """

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
                #'interval': 7,
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

            # post the pipeline to the api
            post_pipeline = requests.post(
                url,
                headers={'x-api-key': skywatch_key},
                json=params)
            post_response = post_pipeline.json()

            print(post_response)

            # if no errors in api response,
            # save form as object and fill in other fields
            if post_pipeline.status_code == 201:

                form.save()

                # get the object id
                current_list = List.objects.latest('id')
                id = current_list.id

                api_id = post_response['data']['id']
                current_list.created_by = user
                current_list.status = 'pending'
                current_list.api_id = api_id
                current_list.aoi_area = round(float((post_response['data']['area_km2'])), 2)
                current_list.save()

                # direct user to detail view of this model
                return redirect(reverse('detail_view', args=[id]))

            # if api cannot be reached
            # return user to homepage with error message
            else:

                if post_pipeline.status_code == 400:

                    context = {
                        'error': "Response 400:  there was an error when submitting the form"
                    }

                else:

                    context = {
                        'error': "Response 500:  we could not reach the API just now.  Please try again later."
                    }

                return render(request, 'index.html', context)

        # if form is not valid
        # return to form
        else:
            
            # fill in form details with users values
            context = {
                'form': form,
                'mapbox_key': mapbox_key,
                'error': "Error: some parameters were not valid.  Please check all parameters meet requirements.",
            }

            return render(request, 'create_pipeline.html', context)

    form = CreateList()

    context = {
        'form': form,
        'mapbox_key': mapbox_key,
    }

    return render(request, 'create_pipeline.html', context)


def my_pipelines(request):
    """
    A view to fetch the user's pipelines and
    display them by status.

    Parameters:
    Request - user's submitted form.

    Returns:
    List of pipelines for user.
    """

    user = str(request.user)

    active_pipelines = List.objects.filter(status='active',
        created_by=user).order_by('date_created')

    complete_pipelines = List.objects.filter(status='complete',
        created_by=user).order_by('date_created')

    pending_pipelines = List.objects.filter(status='pending',
        created_by=user).order_by('date_created')

    saved_pipelines = List.objects.filter(status='saved',
        created_by=user).order_by('date_created')

    context = {
        'active': active_pipelines,
        'complete': complete_pipelines,
        'pending': pending_pipelines,
        'saved': saved_pipelines,
    }

    return render(request, 'my_pipelines.html', context)


def detail_view(request, id):
    """
    A view to fetch the instance of the pipeline
    and relating results and display the information

    Parameters:
    request (object): HTTP request object.
    id: pipeline instance

    Returns:
    Detailed view of pipeline and relating results
    """

    context = {
        'pipeline': List.objects.get(id=id),
        'results': Result.objects.filter(pipeline_id=id).order_by('interval_start_date'),
        'mapbox_key': mapbox_key,
    }

    print(List.objects.get(id=id).start_date)

    return render(request, 'detail_view.html', context)


def delete(request, id):
    """
    A view to fetch the instance of the pipeline
    and delete it if confirmed by user.

    Parameters:
    request (object): HTTP request object.
    id: pipeline instance

    Returns:
    Confirmation of deleted pipeline (delete_conf)
    """

    # get object to delete api id to post to api
    pipeline_id = List.objects.get(id=id).api_id

    # delete from api
    url = (f'https://api.skywatch.co/earthcache/pipelines/{pipeline_id}')

    delete_pipeline = requests.delete(
        url,
        headers={
            'x-api-key': skywatch_key
        }
    )

    print(delete_pipeline)

    # get all related results
    results_to_delete = Result.objects.filter(pipeline_id=id)

    # delete all results
    for result in results_to_delete:
        result.delete()

    return redirect(reverse('delete_feedback', args=[id]))


def delete_view(request, id):
    """
    A view display the name of the pipeline
    to be deleted, and request from user confirmation
    of delete.

    Parameters:
    request (object): HTTP request object.
    id: pipeline instance

    Returns:
    Confirmation of deleted pipeline (delete_conf)
    """

    # get pipeline to delete
    pipeline = List.objects.get(id=id)

    context = {
        'pipeline': pipeline,
    }

    return render(request, 'delete_view.html', context)


def delete_feedback(request, id):

    object_to_delete = List.objects.get(id=id)

    context = {
        'pipeline': object_to_delete,
    }

    object_to_delete.delete()

    return render(request, 'delete_conf.html', context)


def update(request, id):
    """
    A view to refresh the details of the pipeline,
    calling the API to return updated details of results.

    Parameters:
    request (object): HTTP request object.
    id: pipeline instance

    Returns:
    Updated information from API for results.
    """

    time_now = timezone.now()
    time = str(datetime.datetime.now())

    # get the api id of this object to post to api
    api_id = List.objects.get(id=id).api_id

    # api url to update the pipeline status
    url = (f'https://api.skywatch.co/earthcache/pipelines/{api_id}')
    list_response = requests.get(
        url,
        headers={
            'x-api-key': skywatch_key,
        }
    ).json()

    # get object to update
    update_list = List.objects.get(id=id)

    # update fields in List object  & save
    update_list.results_updated = time_now
    update_list.status = list_response['data']['status']
    update_list.save()

    url = (f'https://api.skywatch.co/earthcache/pipelines/{api_id}/interval_results')

    results_response = requests.get(
        url,
        headers={
            'x-api-key': skywatch_key
        }
    ).json()

    print(results_response)

    # update fields in List object & save
    update_list.num_results = len(results_response['data'])

    # count how many images have been found for this pipeline
    num_images = 0
    for i in results_response['data']:
        if len(i['results']) == 1:
            num_images += 1

    update_list.num_images = num_images
    update_list.save()

    # if there are no results created yet for this List object
    # create them
    if len(Result.objects.filter(pipeline_id=id)) == 0:

        for i in results_response['data']:

            # create new result object
            new_result = Result(
                pipeline_id=update_list,
                created_at=i['created_at'],
                updated_at=i['updated_at'],
                api_pipeline_id=i['pipeline_id'],
                status=i['status'],
                output_id=i['output_id'],
                message=i['message'],
                interval_start_date=i['interval']['start_date'],
                interval_end_date=i['interval']['end_date'],
            )

            # save the newly created result
            new_result.save()

            # if an image is found for each interval
            if len(i['results']) > 0:

                new_result.image_created_at = i['results'][0]['created_at']
                new_result.image_updated_at = i['results'][0]['updated_at']
                new_result.image_preview_url = i['results'][0]['preview_url']
                new_result.image_visual_url = i['results'][0]['visual_url']
                new_result.image_analytics_url = i['results'][0]['analytics_url']
                new_result.image_metadata_url = i['results'][0]['metadata_url']
                new_result.image_size = i['results'][0]['metadata']['size_in_mb']
                new_result.image_valid_pixels_per = i['results'][0]['metadata']['valid_pixels_percentage']
                new_result.image_source = i['results'][0]['metadata']['source']
                new_result.scene_height = i['overall_metadata']['scene_height']
                new_result.scene_width = i['overall_metadata']['scene_width']
                new_result.filled_area = i['overall_metadata']['filled_area_km2']
                new_result.aoi_area_per = i['overall_metadata']['filled_area_percentage_of_aoi']
                new_result.cloud_cover_per = i['overall_metadata']['cloud_cover_percentage']
                new_result.aoi_cloud_cover_per = i['overall_metadata']['cloud_cover_percentage_of_aoi']
                new_result.visible_area = i['overall_metadata']['visible_area_km2']
                new_result.aoi_visible_area_per = i['overall_metadata']['visible_area_percentage_of_aoi']

            # save the newly created result
            new_result.save()

    # if there are already results created for this List object
    # update them
    else:

        for i in results_response['data']:

            # get the object to update
            # use unique pipeline id, and interval dates
            # to get the correct result object
            update_result = Result.objects.get(
                pipeline_id=id,
                interval_start_date=i['interval']['start_date'],
                interval_end_date=i['interval']['end_date'])

            update_result.updated_at = i['updated_at']
            update_result.status = i['status']
            update_result.message = i['message']

            # if there are now images
            # add images & data to result object
            if len(i['results']) > 0:

                update_result.image_created_at = i['results'][0]['capture_time']
                update_result.image_updated_at = i['results'][0]['updated_at']
                update_result.image_preview_url = i['results'][0]['preview_url']
                update_result.image_visual_url = i['results'][0]['visual_url']
                update_result.image_analytics_url = i['results'][0]['analytics_url']
                update_result.image_metadata_url = i['results'][0]['metadata_url']
                update_result.image_size = i['results'][0]['metadata']['size_in_mb']
                update_result.image_valid_pixels_per = i['results'][0]['metadata']['valid_pixels_percentage']
                update_result.image_source = i['results'][0]['metadata']['source']
                update_result.scene_height = i['overall_metadata']['scene_height']
                update_result.scene_width = i['overall_metadata']['scene_width']
                update_result.filled_area = i['overall_metadata']['filled_area_km2']
                update_result.aoi_area_per = i['overall_metadata']['filled_area_percentage_of_aoi']
                update_result.cloud_cover_per = i['overall_metadata']['cloud_cover_percentage']
                update_result.aoi_cloud_cover_per = i['overall_metadata']['cloud_cover_percentage_of_aoi']
                update_result.visible_area = i['overall_metadata']['visible_area_km2']
                update_result.aoi_visible_area_per = i['overall_metadata']['visible_area_percentage_of_aoi']

                # save latest image as featured image on my_pipelines.html
                update_list.featured_image = i['results'][0]['preview_url']
                update_list.save()

            # save the updated result
            update_result.save()

    return redirect(reverse('detail_view', args=[id]))
