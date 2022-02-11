# Import 3rd party

# Import django
from django.shortcuts import render, redirect, reverse
import requests
#from django.conf import settings
#from django.contrib.auth.models import User
import datetime
from django.utils import timezone
#import pytz

# Import local
from .models import List, Result
from .forms import CreateList, UpdateList
import os
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

    user = str(request.user)
    edit_time = timezone.now()

    users_pipelines = List.objects.filter(created_by=user)

    this_pipeline = List.objects.get(id=id)
    this_pipeline.time_edited = edit_time
    this_pipeline.save()

    form = UpdateList(instance=this_pipeline)

    if request.method == 'POST':

        form = UpdateList(request.POST, instance=this_pipeline)

        if form.is_valid():

            form.save()

        # else

        return redirect(reverse('detail_view', args=[id]))

    context = {
        'form': form,
        'pipeline': this_pipeline,
        'users_pipelines': users_pipelines,
    }

    return render(request, 'edit_pipeline.html', context)


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

    user = str(request.user)

    if request.method == 'POST':

        form = CreateList(request.POST)

        if form.is_valid():

            format_aoi = form.cleaned_data['aoi']['features'][0]['geometry']

            url = 'https://api.skywatch.co/earthcache/pipelines'

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
                # very important - max cost must be kept to 0!!
                'max_cost': 0,
                'cloud_cover_percentage': form.cleaned_data['cloud_cover'],
                'min_aoi_coverage_percentage': 50,
                'result_delivery': {
                    'max_latency': form.cleaned_data['interval'],
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

            post_pipeline = requests.post(
                url,
                headers={'x-api-key': skywatch_key},
                json=params)
            post_response = post_pipeline.json()

            if post_pipeline.status_code == 201:

                form.save()
                current_list = List.objects.latest('id')
                id = current_list.id
                api_id = post_response['data']['id']
                current_list.created_by = user
                current_list.status = 'pending'
                current_list.api_id = api_id
                area = round(float((post_response['data']['area_km2'])), 2)
                current_list.aoi_area = area
                current_list.save()

                return redirect(reverse('detail_view', args=[id]))

            else:

                if post_pipeline.status_code == 400:

                    form = CreateList()
                    context = {
                        'form': form,
                        'error': "Response 400:"
                        "there was an error when submitting the form"
                    }

                else:

                    form = CreateList()
                    context = {
                        'form': form,
                        'error': "Response 500:"
                        "we could not reach the API just now."
                        "Please try again later."
                    }

                return render(request, 'index.html', context)

        else:

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

    active_pipelines = List.objects.filter(status='active', created_by=user)
    active_pipelines.order_by('date_created')

    complete_pipelines = List.objects.filter(status='complete',
                                             created_by=user)
    complete_pipelines.order_by('date_created')

    pending_pipelines = List.objects.filter(status='pending', created_by=user)
    pending_pipelines.order_by('date_created')

    context = {
        'active': active_pipelines,
        'complete': complete_pipelines,
        'pending': pending_pipelines,
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

    user = str(request.user)
    users_pipelines = List.objects.filter(created_by=user)

    all_dates = []
    complete_intervals = []
    current_interval = []
    future_intervals = []
    image_dates = []
    today = datetime.date.today()

    for result in Result.objects.filter(pipeline_id=id):

        s_date = result.interval_start_date
        start_date = s_date.strftime("%d-%m-%Y")

        e_date = result.interval_end_date
        end_date = e_date.strftime("%d-%m-%Y")

        if s_date < today and e_date < today:
            complete_intervals.append(start_date)
            complete_intervals.append(end_date)
            result.status = "complete"
            result.save()

        if s_date <= today and today <= e_date:
            current_interval.append(start_date)
            current_interval.append(end_date)
            result.status = "current"
            result.save()

        else:
            all_dates.append(start_date)
            all_dates.append(end_date)

        if s_date > today and e_date > today:
            future_intervals.append(start_date)
            future_intervals.append(end_date)
            result.status = "future"
            result.save()

        if result.image_created_at is not None:
            image_taken = result.image_created_at.strftime("%d-%m-%Y")
            image_dates.append(image_taken)

    pipeline_s_date = List.objects.get(id=id).start_date
    if pipeline_s_date > today:
        message = "not started"
    else:
        message = ""

    results = Result.objects.filter(pipeline_id=id)
    result = results.order_by('interval_start_date')

    context = {
        'pipeline': List.objects.get(id=id),
        'results': result,
        'mapbox_key': mapbox_key,
        'current': current_interval,
        'complete': complete_intervals,
        'future': future_intervals,
        'images': image_dates,
        'all_dates': all_dates,
        'message': message,
        'users_pipelines': users_pipelines,
    }

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

    pipeline_id = List.objects.get(id=id).api_id

    url = (f'https://api.skywatch.co/earthcache/pipelines/{pipeline_id}')

    delete_pipeline = requests.delete(
        url,
        headers={
            'x-api-key': skywatch_key
        }
    )

    results_to_delete = Result.objects.filter(pipeline_id=id)

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

    user = str(request.user)

    users_pipelines = List.objects.filter(created_by=user)

    pipeline = List.objects.get(id=id)

    context = {
        'pipeline': pipeline,
        'users_pipelines': users_pipelines,
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
    #time = datetime.date.today()

    api_id = List.objects.get(id=id).api_id

    url = (f'https://api.skywatch.co/earthcache/pipelines/{api_id}')

    updated_list = requests.get(
        url,
        headers={
            'x-api-key': skywatch_key,
        }
    )

    list_response = updated_list.json()

    if updated_list.status_code == 200 or updated_list.status_code == 201:

        update_list = List.objects.get(id=id)
        update_list.results_updated = time_now
        update_list.status = list_response['data']['status']
        update_list.save()

        url = (f'https://api.skywatch.co/earthcache/pipelines'
               f'/{api_id}/interval_results')

        results_response = requests.get(
            url,
            headers={
                'x-api-key': skywatch_key
            }
        ).json()

        update_list.num_results = len(results_response['data'])

        num_images = 0
        for i in results_response['data']:
            if len(i['results']) == 1:
                num_images += 1

        update_list.num_images = num_images
        update_list.save()

        if len(Result.objects.filter(pipeline_id=id)) == 0:

            for i in results_response['data']:
                new_result = Result(
                    pipeline_id=update_list,
                    created_at=time_now,
                    updated_at=i['updated_at'],
                    api_pipeline_id=i['pipeline_id'],
                    status=i['status'],
                    output_id=i['output_id'],
                    message=i['message'],
                    interval_start_date=i['interval']['start_date'],
                    interval_end_date=i['interval']['end_date'],
                )

                new_result.save()

                if len(i['results']) > 0:

                    ires = i['results'][0]
                    imet = i['overall_metadata']

                    new_result.image_created_at = ires['capture_time']
                    new_result.image_updated_at = ires['updated_at']
                    new_result.image_preview_url = ires['preview_url']
                    new_result.image_visual_url = ires['visual_url']
                    new_result.image_analytics_url = ires['analytics_url']
                    new_result.image_metadata_url = ires['metadata_url']
                    new_result.image_size = ires['metadata']['size_in_mb']
                    ires_valid = ires['metadata']['valid_pixels_percentage']
                    new_result.image_valid_pixels_per = ires_valid
                    new_result.image_source = ires['metadata']['source']
                    new_result.scene_height = imet['scene_height']
                    new_result.scene_width = imet['scene_width']
                    new_result.filled_area = imet['filled_area_km2']
                    imet_filled = imet['filled_area_percentage_of_aoi']
                    new_result.aoi_area_per = imet_filled
                    new_result.cloud_cover_per = imet['cloud_cover_percentage']
                    imet_cl_per = imet['cloud_cover_percentage_of_aoi']
                    new_result.aoi_cloud_cover_per = imet_cl_per
                    new_result.visible_area = imet['visible_area_km2']
                    imet_vis = imet['visible_area_percentage_of_aoi']
                    new_result.aoi_visible_area_per = imet_vis

                    update_list.featured_image = i['results'][0]['preview_url']
                    update_list.save()

                new_result.save()

        else:

            for i in results_response['data']:

                update_result = Result.objects.get(
                    pipeline_id=id,
                    interval_start_date=i['interval']['start_date'],
                    interval_end_date=i['interval']['end_date'])

                update_result.updated_at = i['updated_at']
                update_result.status = i['status']
                update_result.message = i['message']

                if len(i['results']) > 0:

                    ires = i['results'][0]
                    imet = i['overall_metadata']

                    update_result.image_created_at = ires['capture_time']
                    update_result.image_updated_at = ires['updated_at']
                    update_result.image_preview_url = ires['preview_url']
                    update_result.image_visual_url = ires['visual_url']
                    update_result.image_analytics_url = ires['analytics_url']
                    update_result.image_metadata_url = ires['metadata_url']
                    update_result.image_size = ires['metadata']['size_in_mb']
                    ires_valid = ires['metadata']['valid_pixels_percentage']
                    update_result.image_valid_pixels_per = ires_valid
                    update_result.image_source = ires['metadata']['source']
                    update_result.scene_height = imet['scene_height']
                    update_result.scene_width = imet['scene_width']
                    update_result.filled_area = imet['filled_area_km2']
                    imet_filled = imet['filled_area_percentage_of_aoi']
                    update_result.aoi_area_per = imet_filled
                    imet_cl = imet['cloud_cover_percentage']
                    update_result.cloud_cover_per = imet_cl
                    imet_cl_per = imet['cloud_cover_percentage_of_aoi']
                    update_result.aoi_cloud_cover_per = imet_cl_per
                    update_result.visible_area = imet['visible_area_km2']
                    imet_vis = imet['visible_area_percentage_of_aoi']
                    update_result.aoi_visible_area_per = imet_vis

                    update_list.featured_image = i['results'][0]['preview_url']
                    update_list.save()

                update_result.save()

    else:

        if updated_list.status_code == 404:
            error = "Error 404:  unfortunately we could not find your pipeline to update."
        elif updated_list.status_code == 400 or updated_list.status_code == 401 or updated_list.status_code == 413 or updated_list.status_code == 415:
            error = "Error 400:  some of your pipeline details were not correct.  We can not update your pipeline."
        else:
            error = "Error 504: the server timed out.  Please try again later."

        context = {
            'error': error
        }

        return redirect(reverse('detail_view', args=[id]), context)

    return redirect(reverse('detail_view', args=[id]))
