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


# display the homepage
def homepage(request):
    return render(request, 'index.html')

# display the discover page
def discover(request):
    return render(request, 'discover.html')


# edit the pipeline (UPDATE)
def edit(request, id):

    # get the object to update
    this_pipeline = List.objects.get(id=id)

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


# create a pipeline (CREATE)
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
                id = current_list.id

                api_id = post_response['data']['id']
                # current_list.slug = slugify(pipeline_name)
                current_list.created_by = user
                current_list.status = 'pending'
                current_list.api_id = api_id
                current_list.save()

                # direct user to detail view of this model
                return redirect(reverse('detail_view', args=[id]))

        # if form is not valid
        # return to form
        else:
            print('NOT VALID')
            print(form.errors)

    form = CreateList()

    context = {
        'form': form,
    }

    return render(request, 'create_pipeline.html', context)


# display all the user's models
def my_pipelines(request):

    user = str(request.user)

    active_pipelines = List.objects.filter(status='active', created_by=user).order_by('date_created')
    complete_pipelines = List.objects.filter(status='complete',
        created_by=user).order_by('date_created')
    pending_pipelines = List.objects.filter(status='pending',
        created_by=user).order_by('date_created')
    saved_pipelines = List.objects.filter(status='saved',
        created_by=user).order_by('date_created')

    num_active_pipelines = len(active_pipelines)
    num_complete_pipelines = len(complete_pipelines)
    num_pending_pipelines = len(pending_pipelines)
    num_saved_pipelines = len(saved_pipelines)

    context = {
        'active': active_pipelines,
        'complete': complete_pipelines,
        'pending': pending_pipelines,
        'saved': saved_pipelines,
        'active_num': num_active_pipelines,
        'complete_num': num_complete_pipelines,
        'pending_num': num_pending_pipelines,
        'saved_num': num_saved_pipelines,
    }

    return render(request, 'my_pipelines.html', context)


# display view of this object (READ)
def detail_view(request, id):

    context = {
        'pipeline': List.objects.get(id=id),
        'results': Result.objects.filter(pipeline_id=id),
        'mapbox_key': mapbox_key,
    }

    return render(request, 'detail_view.html', context)


# delete the pipeline (both from models & in api) (DELETE)
def delete(request, id):

    # get object to delete
    object_to_delete = List.objects.get(id=id)

    # get object to delete api id to post to api
    pipeline_id = List.objects.get(id=id).api_id

    ## try except
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

    # delete object
    object_to_delete.delete() 

    # return redirect(reverse('pipeline_deleted', args=[id]))
    return render(request, 'my_pipelines.html')


# display the delete page
def delete_view(request, id):

    # get pipeline to delete
    pipeline = List.objects.get(id=id)

    context = {
        'pipeline': pipeline,
    }

    return render(request, 'delete_view.html', context)


# refresh the pipeline from the api
# this is not the UPDATE aspect of CRUD (see views.edit)
def update(request, id):

    time_now = timezone.now()
    time = str(datetime.datetime.now())

    # get the api id of this object to post to api
    api_id = List.objects.get(id=id).api_id

    # # api url to update the pipeline status
    # url = (f'https://api.skywatch.co/earthcache/pipelines/{api_id}')
    # list_response = requests.get(
    #     url,
    #     headers={
    #         'x-api-key': skywatch_key,
    #     }
    # ).json()

    # get object to update
    update_list = List.objects.get(id=id)

    # update fields in List object  & save
    # update_list.results_updated = time
    # update_list.status = list_response['data']['status']
    # update_list.save()

    # url = (f'https://api.skywatch.co/earthcache/pipelines/{api_id}/interval_results')

    # results_response = requests.get(
    #     url,
    #     headers={
    #         'x-api-key': skywatch_key
    #     }
    # ).json()

    results_response = {'data': [{'id': '3624f851-e9bb-4f28-ba40-a3f48d05d793', 'created_at': '2022-01-20T14:31:24.857634+0000', 'updated_at': '2022-01-20T14:43:03.060805+0000', 'pipeline_id': 'fdfaf5c8-79fe-11ec-b876-62e39cd2349d', 'output_id': '1f0db8b2-b4d4-11e7-a775-a6fe70ce62b1', 'status': 'complete', 'message': 'Processing complete. 1 result available', 'interval': {'start_date': '2021-12-31', 'end_date': '2021-12-31'}, 'total_interval_cost': 0.0, 'overall_metadata': {'scene_height': 1187, 'scene_width': 1372, 'filled_area_km2': 88.22, 'filled_area_percentage_of_aoi': 97.0, 'cloud_cover_percentage': 0.0, 'cloud_cover_percentage_of_aoi': 1.0, 'visible_area_km2': 87.52, 'visible_area_percentage': 54.0, 'visible_area_percentage_of_aoi': 95.79}, 'results': [{'created_at': '2022-01-20T15:04:38.899562', 'updated_at': '2022-01-20T14:43:01.703174+0000', 'preview_url': 'https://s3-us-west-2.amazonaws.com/aoi-processed-images-prod/fdfaf5c8-79fe-11ec-b876-62e39cd2349d/cffae7be-c502-435d-8b0b-9880f63894cc/preview/SKYWATCH_S2_MS_20211231T0830_FCU_Tile_0_0_X2V5_preview.png', 'visual_url': 'https://s3-us-west-2.amazonaws.com/aoi-processed-images-prod/fdfaf5c8-79fe-11ec-b876-62e39cd2349d/cffae7be-c502-435d-8b0b-9880f63894cc/visual/SKYWATCH_S2_MS_20211231T0830_FCU_Tile_0_0_X2V5_visual.png', 'analytics_url': 'https://s3-us-west-2.amazonaws.com/aoi-processed-images-prod/fdfaf5c8-79fe-11ec-b876-62e39cd2349d/cffae7be-c502-435d-8b0b-9880f63894cc/analytic/SKYWATCH_S2_MS_20211231T0830_FCU_Tile_0_0_X2V5.tif', 'metadata_url': 'https://s3-us-west-2.amazonaws.com/aoi-processed-images-prod/fdfaf5c8-79fe-11ec-b876-62e39cd2349d/cffae7be-c502-435d-8b0b-9880f63894cc/metadata/SKYWATCH_S2_MS_20211231T0830_FCU_Tile_0_0_X2V5_metadata.json', 'vector_files': [{'name': 'cloud_mask_vector', 'description': 'GeoJSON vector mask of cloud cover', 'uri': 'https://s3-us-west-2.amazonaws.com/aoi-processed-images-prod/fdfaf5c8-79fe-11ec-b876-62e39cd2349d/cffae7be-c502-435d-8b0b-9880f63894cc/vector_file/SKYWATCH_S2_MS_20211231T0830_FCU_Tile_0_0_X2V5_flags_vector.json'}], 'raster_files': [{'name': 'cloud_mask_raster', 'description': 'GeoTiff mask of cloud cover', 'uri': 'https://s3-us-west-2.amazonaws.com/aoi-processed-images-prod/fdfaf5c8-79fe-11ec-b876-62e39cd2349d/cffae7be-c502-435d-8b0b-9880f63894cc/raster_file/SKYWATCH_S2_MS_20211231T0830_FCU_Tile_0_0_X2V5_masks.tif'}, {'name': 'visual_overlays', 'description': 'Visual PNG image with overlays', 'uri': 'https://s3-us-west-2.amazonaws.com/aoi-processed-images-prod/fdfaf5c8-79fe-11ec-b876-62e39cd2349d/cffae7be-c502-435d-8b0b-9880f63894cc/raster_file/SKYWATCH_S2_MS_20211231T0830_FCU_Tile_0_0_X2V5_visual_overlays.png'}], 'capture_time': '2021-12-31T08:30:40.976125+0000', 'metadata': {'processing_applied': {'atmospheric_correction_toa': False, 'pansharpening': False, 'cloud_masking': False, 'haze_masking': False}, 'bands': [{'name': 'short-wave-infrared-2', 'no_data_value': 0, 'data_type': 'float32', 'unit': 'toa_reflectance', 'spectral_wavelength': None, 'raster_width': 1372, 'raster_height': 1187}, {'name': 'short-wave-infrared-1', 'no_data_value': 0, 'data_type': 'float32', 'unit': 'toa_reflectance', 'spectral_wavelength': None, 'raster_width': 1372, 'raster_height': 1187}, {'name': 'red', 'no_data_value': 0, 'data_type': 'float32', 'unit': 'toa_reflectance', 'spectral_wavelength': None, 'raster_width': 1372, 'raster_height': 1187}, {'name': 'flags', 'no_data_value': 255, 'data_type': 'uint8', 'unit': 'bit', 'spectral_wavelength': None, 'raster_width': 1372, 'raster_height': 1187}], 'resolution_y': 10, 'resolution_x': 10, 'map_crs': 'GEOGCS[WGS 84,   DATUM[World Geodetic System 1984,     SPHEROID[WGS 84, 6378137.0, 298.257223563, AUTHORITY[EPSG,7030]],     AUTHORITY[EPSG,6326]],   PRIMEM[Greenwich, 0.0, AUTHORITY[EPSG,8901]],   UNIT[degree, 0.017453292519943295],   AXIS[Geodetic longitude, EAST],   AXIS[Geodetic latitude, NORTH],   AUTHORITY[EPSG,4326]]', 'sensor_mode': 'Strip', 'source': 'Sentinel-2', 'cloud_cover_percentage': 0, 'valid_pixels_percentage': 54, 'name': 'SKYWATCH_S2_MS_20211231T0830_FCU_Tile_0_0_X2V5', 'size_in_mb': 21, 'corner_coordinates': [[36.1880719337536, 33.56586409114093], [36.33563310851325, 33.56586409114093], [36.33563310851325, 33.45893085036887], [36.1880719337536, 33.45893085036887], [36.1880719337536, 33.56586409114093]]}}], 'alternate_search_results': [{'index': 0, 'search_result_id': '1ddbdb00-bacd-4fd8-8c80-46ca6b388014', 'source': 'Sentinel-2', 'capture_date': '2021-12-31', 'resolution': 10.0, 'price_per_km2': 0.0, 'max_interval_cost': 0.0, 'aoi_coverage_percentage': 95.78, 'filled_coverage_percentage': 97, 'processing_status': 'delivered'}, {'index': 1, 'search_result_id': '7d9f201a-b2d1-4e1b-99ff-2a33e2238848', 'source': 'Sentinel-2', 'capture_date': '2021-12-31', 'resolution': 10.0, 'price_per_km2': 0, 'max_interval_cost': 0, 'aoi_coverage_percentage': None, 'filled_coverage_percentage': None, 'processing_status': 'not processed - low priority'}]}, {'id': '3624f851-e9bb-4f28-ba40-a3f48d05d793', 'created_at': '2022-01-20T14:31:24.857634+0000', 'updated_at': '2022-01-20T14:41:38.162601+0000', 'pipeline_id': 'fdfaf5c8-79fe-11ec-b876-62e39cd2349d', 'output_id': '1f0db8b2-b4d4-11e7-a775-a6fe70ce62b1', 'status': 'complete', 'message': 'Processing complete', 'interval': {'start_date': '2022-01-01', 'end_date': '2022-01-01'}, 'total_interval_cost': None, 'overall_metadata': {'scene_height': None, 'scene_width': None, 'filled_area_km2': None, 'filled_area_percentage_of_aoi': None, 'cloud_cover_percentage': None, 'cloud_cover_percentage_of_aoi': None, 'visible_area_km2': None, 'visible_area_percentage': None, 'visible_area_percentage_of_aoi': None}, 'results': [], 'alternate_search_results': []}, {'id': '3624f851-e9bb-4f28-ba40-a3f48d05d793', 'created_at': '2022-01-20T14:31:24.857634+0000', 'updated_at': '2022-01-20T14:41:39.357633+0000', 'pipeline_id': 'fdfaf5c8-79fe-11ec-b876-62e39cd2349d', 'output_id': '1f0db8b2-b4d4-11e7-a775-a6fe70ce62b1', 'status': 'complete', 'message': 'Processing complete', 'interval': {'start_date': '2022-01-02', 'end_date': '2022-01-02'}, 'total_interval_cost': None, 'overall_metadata': {'scene_height': None, 'scene_width': None, 'filled_area_km2': None, 'filled_area_percentage_of_aoi': None, 'cloud_cover_percentage': None, 'cloud_cover_percentage_of_aoi': None, 'visible_area_km2': None, 'visible_area_percentage': None, 'visible_area_percentage_of_aoi': None}, 'results': [], 'alternate_search_results': []}, {'id': '3624f851-e9bb-4f28-ba40-a3f48d05d793', 'created_at': '2022-01-20T14:31:24.857634+0000', 'updated_at': '2022-01-20T14:41:41.882354+0000', 'pipeline_id': 'fdfaf5c8-79fe-11ec-b876-62e39cd2349d', 'output_id': '1f0db8b2-b4d4-11e7-a775-a6fe70ce62b1', 'status': 'complete', 'message': 'Processing complete', 'interval': {'start_date': '2022-01-03', 'end_date': '2022-01-03'}, 'total_interval_cost': None, 'overall_metadata': {'scene_height': None, 'scene_width': None, 'filled_area_km2': None, 'filled_area_percentage_of_aoi': None, 'cloud_cover_percentage': None, 'cloud_cover_percentage_of_aoi': None, 'visible_area_km2': None, 'visible_area_percentage': None, 'visible_area_percentage_of_aoi': None}, 'results': [], 'alternate_search_results': []}, {'id': '3624f851-e9bb-4f28-ba40-a3f48d05d793', 'created_at': '2022-01-20T14:31:24.857634+0000', 'updated_at': '2022-01-20T14:41:42.762440+0000', 'pipeline_id': 'fdfaf5c8-79fe-11ec-b876-62e39cd2349d', 'output_id': '1f0db8b2-b4d4-11e7-a775-a6fe70ce62b1', 'status': 'complete', 'message': 'Processing complete', 'interval': {'start_date': '2022-01-04', 'end_date': '2022-01-04'}, 'total_interval_cost': None, 'overall_metadata': {'scene_height': None, 'scene_width': None, 'filled_area_km2': None, 'filled_area_percentage_of_aoi': None, 'cloud_cover_percentage': None, 'cloud_cover_percentage_of_aoi': None, 'visible_area_km2': None, 'visible_area_percentage': None, 'visible_area_percentage_of_aoi': None}, 'results': [], 'alternate_search_results': []}, {'id': '3624f851-e9bb-4f28-ba40-a3f48d05d793', 'created_at': '2022-01-20T14:31:24.857634+0000', 'updated_at': '2022-01-20T14:43:13.860914+0000', 'pipeline_id': 'fdfaf5c8-79fe-11ec-b876-62e39cd2349d', 'output_id': '1f0db8b2-b4d4-11e7-a775-a6fe70ce62b1', 'status': 'complete', 'message': 'Processing complete. 1 result available', 'interval': {'start_date': '2022-01-05', 'end_date': '2022-01-05'}, 'total_interval_cost': 0.0, 'overall_metadata': {'scene_height': 1187, 'scene_width': 1372, 'filled_area_km2': 88.22, 'filled_area_percentage_of_aoi': 97.0, 'cloud_cover_percentage': 23.0, 'cloud_cover_percentage_of_aoi': 42.0, 'visible_area_km2': 50.13, 'visible_area_percentage': 31.0, 'visible_area_percentage_of_aoi': 54.87}, 'results': [{'created_at': '2022-01-20T15:04:38.900029', 'updated_at': '2022-01-20T14:43:12.523237+0000', 'preview_url': 'https://s3-us-west-2.amazonaws.com/aoi-processed-images-prod/fdfaf5c8-79fe-11ec-b876-62e39cd2349d/33d646bc-3ea1-40f8-a1bf-f2e2900eefeb/preview/SKYWATCH_S2_MS_20220105T0830_FCU_Tile_0_0_Hvn7_preview.png', 'visual_url': 'https://s3-us-west-2.amazonaws.com/aoi-processed-images-prod/fdfaf5c8-79fe-11ec-b876-62e39cd2349d/33d646bc-3ea1-40f8-a1bf-f2e2900eefeb/visual/SKYWATCH_S2_MS_20220105T0830_FCU_Tile_0_0_Hvn7_visual.png', 'analytics_url': 'https://s3-us-west-2.amazonaws.com/aoi-processed-images-prod/fdfaf5c8-79fe-11ec-b876-62e39cd2349d/33d646bc-3ea1-40f8-a1bf-f2e2900eefeb/analytic/SKYWATCH_S2_MS_20220105T0830_FCU_Tile_0_0_Hvn7.tif', 'metadata_url': 'https://s3-us-west-2.amazonaws.com/aoi-processed-images-prod/fdfaf5c8-79fe-11ec-b876-62e39cd2349d/33d646bc-3ea1-40f8-a1bf-f2e2900eefeb/metadata/SKYWATCH_S2_MS_20220105T0830_FCU_Tile_0_0_Hvn7_metadata.json', 'vector_files': [{'name': 'cloud_mask_vector', 'description': 'GeoJSON vector mask of cloud cover', 'uri': 'https://s3-us-west-2.amazonaws.com/aoi-processed-images-prod/fdfaf5c8-79fe-11ec-b876-62e39cd2349d/33d646bc-3ea1-40f8-a1bf-f2e2900eefeb/vector_file/SKYWATCH_S2_MS_20220105T0830_FCU_Tile_0_0_Hvn7_flags_vector.json'}], 'raster_files': [{'name': 'cloud_mask_raster', 'description': 'GeoTiff mask of cloud cover', 'uri': 'https://s3-us-west-2.amazonaws.com/aoi-processed-images-prod/fdfaf5c8-79fe-11ec-b876-62e39cd2349d/33d646bc-3ea1-40f8-a1bf-f2e2900eefeb/raster_file/SKYWATCH_S2_MS_20220105T0830_FCU_Tile_0_0_Hvn7_masks.tif'}, {'name': 'visual_overlays', 'description': 'Visual PNG image with overlays', 'uri': 'https://s3-us-west-2.amazonaws.com/aoi-processed-images-prod/fdfaf5c8-79fe-11ec-b876-62e39cd2349d/33d646bc-3ea1-40f8-a1bf-f2e2900eefeb/raster_file/SKYWATCH_S2_MS_20220105T0830_FCU_Tile_0_0_Hvn7_visual_overlays.png'}], 'capture_time': '2022-01-05T08:30:46.724309+0000', 'metadata': {'processing_applied': {'atmospheric_correction_toa': False, 'pansharpening': False, 'cloud_masking': False, 'haze_masking': False}, 'bands': [{'name': 'short-wave-infrared-2', 'no_data_value': 0, 'data_type': 'float32', 'unit': 'toa_reflectance', 'spectral_wavelength': None, 'raster_width': 1372, 'raster_height': 1187}, {'name': 'short-wave-infrared-1', 'no_data_value': 0, 'data_type': 'float32', 'unit': 'toa_reflectance', 'spectral_wavelength': None, 'raster_width': 1372, 'raster_height': 1187}, {'name': 'red', 'no_data_value': 0, 'data_type': 'float32', 'unit': 'toa_reflectance', 'spectral_wavelength': None, 'raster_width': 1372, 'raster_height': 1187}, {'name': 'flags', 'no_data_value': 255, 'data_type': 'uint8', 'unit': 'bit', 'spectral_wavelength': None, 'raster_width': 1372, 'raster_height': 1187}], 'resolution_y': 10, 'resolution_x': 10, 'map_crs': 'GEOGCS[WGS 84,   DATUM[World Geodetic System 1984,     SPHEROID[WGS 84, 6378137.0, 298.257223563, AUTHORITY[EPSG,7030]],     AUTHORITY[EPSG,6326]],   PRIMEM[Greenwich, 0.0, AUTHORITY[EPSG,8901]],   UNIT[degree, 0.017453292519943295],   AXIS[Geodetic longitude, EAST],   AXIS[Geodetic latitude, NORTH],   AUTHORITY[EPSG,4326]]', 'sensor_mode': 'Strip', 'source': 'Sentinel-2', 'cloud_cover_percentage': 23, 'valid_pixels_percentage': 31, 'name': 'SKYWATCH_S2_MS_20220105T0830_FCU_Tile_0_0_Hvn7', 'size_in_mb': 21, 'corner_coordinates': [[36.1880719337536, 33.56586409114093], [36.33563310851325, 33.56586409114093], [36.33563310851325, 33.45893085036887], [36.1880719337536, 33.45893085036887], [36.1880719337536, 33.56586409114093]]}}], 'alternate_search_results': [{'index': 0, 'search_result_id': 'c32fa215-c5e5-411b-a88e-68cd72849bff', 'source': 'Sentinel-2', 'capture_date': '2022-01-05', 'resolution': 10.0, 'price_per_km2': 0.0, 'max_interval_cost': 0.0, 'aoi_coverage_percentage': 54.86, 'filled_coverage_percentage': 97, 'processing_status': 'delivered'}, {'index': 1, 'search_result_id': '42e8fa35-3f19-4aa0-b705-5a83096e45a2', 'source': 'Sentinel-2', 'capture_date': '2022-01-05', 'resolution': 10.0, 'price_per_km2': 0, 'max_interval_cost': 0, 'aoi_coverage_percentage': None, 'filled_coverage_percentage': None, 'processing_status': 'not processed - low priority'}]}, {'id': '3624f851-e9bb-4f28-ba40-a3f48d05d793', 'created_at': '2022-01-20T14:31:24.857634+0000', 'updated_at': '2022-01-20T14:41:38.743325+0000', 'pipeline_id': 'fdfaf5c8-79fe-11ec-b876-62e39cd2349d', 'output_id': '1f0db8b2-b4d4-11e7-a775-a6fe70ce62b1', 'status': 'complete', 'message': 'Processing complete', 'interval': {'start_date': '2022-01-06', 'end_date': '2022-01-06'}, 'total_interval_cost': None, 'overall_metadata': {'scene_height': None, 'scene_width': None, 'filled_area_km2': None, 'filled_area_percentage_of_aoi': None, 'cloud_cover_percentage': None, 'cloud_cover_percentage_of_aoi': None, 'visible_area_km2': None, 'visible_area_percentage': None, 'visible_area_percentage_of_aoi': None}, 'results': [], 'alternate_search_results': []}, {'id': '3624f851-e9bb-4f28-ba40-a3f48d05d793', 'created_at': '2022-01-20T14:31:24.857634+0000', 'updated_at': '2022-01-20T14:41:42.865476+0000', 'pipeline_id': 'fdfaf5c8-79fe-11ec-b876-62e39cd2349d', 'output_id': '1f0db8b2-b4d4-11e7-a775-a6fe70ce62b1', 'status': 'complete', 'message': 'Processing complete', 'interval': {'start_date': '2022-01-07', 'end_date': '2022-01-07'}, 'total_interval_cost': None, 'overall_metadata': {'scene_height': None, 'scene_width': None, 'filled_area_km2': None, 'filled_area_percentage_of_aoi': None, 'cloud_cover_percentage': None, 'cloud_cover_percentage_of_aoi': None, 'visible_area_km2': None, 'visible_area_percentage': None, 'visible_area_percentage_of_aoi': None}, 'results': [], 'alternate_search_results': []}, {'id': '3624f851-e9bb-4f28-ba40-a3f48d05d793', 'created_at': '2022-01-20T14:31:24.857634+0000', 'updated_at': '2022-01-20T14:41:40.304615+0000', 'pipeline_id': 'fdfaf5c8-79fe-11ec-b876-62e39cd2349d', 'output_id': '1f0db8b2-b4d4-11e7-a775-a6fe70ce62b1', 'status': 'complete', 'message': 'Processing complete', 'interval': {'start_date': '2022-01-08', 'end_date': '2022-01-08'}, 'total_interval_cost': None, 'overall_metadata': {'scene_height': None, 'scene_width': None, 'filled_area_km2': None, 'filled_area_percentage_of_aoi': None, 'cloud_cover_percentage': None, 'cloud_cover_percentage_of_aoi': None, 'visible_area_km2': None, 'visible_area_percentage': None, 'visible_area_percentage_of_aoi': None}, 'results': [], 'alternate_search_results': []}, {'id': '3624f851-e9bb-4f28-ba40-a3f48d05d793', 'created_at': '2022-01-20T14:31:24.857634+0000', 'updated_at': '2022-01-20T14:41:42.199258+0000', 'pipeline_id': 'fdfaf5c8-79fe-11ec-b876-62e39cd2349d', 'output_id': '1f0db8b2-b4d4-11e7-a775-a6fe70ce62b1', 'status': 'complete', 'message': 'Processing complete', 'interval': {'start_date': '2022-01-09', 'end_date': '2022-01-09'}, 'total_interval_cost': None, 'overall_metadata': {'scene_height': None, 'scene_width': None, 'filled_area_km2': None, 'filled_area_percentage_of_aoi': None, 'cloud_cover_percentage': None, 'cloud_cover_percentage_of_aoi': None, 'visible_area_km2': None, 'visible_area_percentage': None, 'visible_area_percentage_of_aoi': None}, 'results': [], 'alternate_search_results': []}], 'pagination': {'per_page': 2000, 'cursor': {'next': None, 'self': '2022-01-20T14:43:03.060805+0000'}}}

    #print(results_response)

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

                new_result.image_created_at = i['results'][0]['created_at'],
                new_result.image_updated_at = i['results'][0]['updated_at'],
                new_result.image_preview_url = i['results'][0]['preview_url'],
                new_result.image_visual_url = i['results'][0]['visual_url'],
                new_result.image_analytics_url = i['results'][0]
                ['analytics_url'],
                new_result.image_metadata_url = i['results'][0]
                ['metadata_url'],
                new_result.image_size = i['results'][0]['metadata']
                ['size_in_mb'],
                new_result.image_valid_pixels_per = i['results'][0]['metadata']
                ['valid_pixels_percentage'],
                new_result.image_source = i['results'][0]['metadata']
                ['source'],
                new_result.scene_height = i['overall_metadata']
                ['scene_height'],
                new_result.scene_width = i['overall_metadata']
                ['scene_width'],
                new_result.filled_area = i['overall_metadata']
                ['filled_area_km'],
                new_result.aoi_area_per = i['overall_metadata']
                ['filled_area_percentage_of_aoi'],
                new_result.cloud_cover_per = i['overall_metadata']
                ['cloud_cover_percentage'],
                new_result.aoi_cloud_cover_per = i['overall_metadata']
                ['cloud_cover_percentage_of_aoi'],
                new_result.visible_area = i['overall_metadata']
                ['visible_area_km2'],
                new_result.aoi_visible_area_per = i['overall_metadata']
                ['visible_area_percentage_of_aoi']

                # save latest image as featured image on my_pipelines.html
                update_list.featured_image = i['results'][0]['preview_url']
                update_list.save()

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
            # add images to result object
            if len(i['results']) > 0:

                # update_result.image_created_at = i['results'][0]
                # ['capture_time']
                # update_result.image_updated_at = i['results'][0]['updated_at']
                update_result.image_preview_url = i['results'][0]['preview_url']
                update_result.image_visual_url = i['results'][0]['visual_url'],
                update_result.image_analytics_url = i['results'][0]
                ['analytics_url'],
                update_result.image_metadata_url = i['results'][0]
                ['metadata_url'],
                update_result.image_size = i['results'][0]['metadata']
                ['size_in_mb'],
                update_result.image_valid_pixels_per = i['results'][0]
                ['metadata']
                ['valid_pixels_percentage'],
                update_result.image_source = i['results'][0]['metadata']
                ['source'],
                update_result.scene_height = i['overall_metadata']
                ['scene_height'],
                update_result.scene_width = i['overall_metadata']
                ['scene_width'],
                update_result.filled_area = i['overall_metadata']
                ['filled_area_km'],
                update_result.aoi_area_per = i['overall_metadata']
                ['filled_area_percentage_of_aoi'],
                update_result.cloud_cover_per = i['overall_metadata']
                ['cloud_cover_percentage'],
                update_result.aoi_cloud_cover_per = i['overall_metadata']
                ['cloud_cover_percentage_of_aoi'],
                update_result.visible_area = i['overall_metadata']
                ['visible_area_km2'],
                update_result.aoi_visible_area_per = i['overall_metadata']
                ['visible_area_percentage_of_aoi']

            # save the updated result
            update_result.save()

    return redirect(reverse('detail_view', args=[id]))
