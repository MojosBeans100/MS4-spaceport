from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe
from cloudinary.models import CloudinaryField

# api interval options
interval = (
    ('1d', 'Daily'),
    ('7d', 'Weekly'),
    ('14d', 'Bi-weekly'),
    ('30d', 'Monthly'),
    ('60d', 'Bi-monthly'),
)

# api output image identifiers
output = (
    ('a8fc3dde-a3e8-11e7-9793-ae4260ee3b4b', 'True Colour'),
    ('1f0db8b2-b4d4-11e7-a775-a6fe70ce62b1', 'False Colour Urban'),
    ('154311a8-582a-11e7-b30d-7291b81e23e3', 'False Colour Infrared'),
    ('c31c1bea-a4be-11e7-8650-3ae5c7149ea7', 'All Optical Bands'),
    ('3cab2e68-b4d4-11e7-a775-a6fe70ce62b1', 'MSAVI2'),
    ('ga23d8a2-8f3d-481c-b7ef-9fa02839aab0', 'Near-infrared'),
)


# list of all pipelines created by all users
class List(models.Model):

    # user parameters
    pipeline_name = models.CharField(max_length=30)
    pipeline_des = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    interval = models.CharField(choices=interval, max_length=15, default=None)
    output_image = models.CharField(choices=output, max_length=100)
    aoi = models.JSONField(null=True)
    cloud_cover = models.CharField(max_length=10)

    # auto generated parameters
    # accept null as many of these parameters are input after
    # form is submitted
    slug = models.SlugField(max_length=200, null=True)
    num_intervals = models.PositiveIntegerField(default=0, null=True)
    date_created = models.DateField(default=timezone.now, null=True)
    aoi_area = models.CharField(max_length=10, null=True)
    created_by = models.CharField(max_length=100, null=True)
    status = models.CharField(max_length=30, null=True)
    api_id = models.CharField(max_length=100, null=True)
    num_results = models.PositiveIntegerField(null=True)
    num_images = models.PositiveIntegerField(null=True)
    results_updated = models.DateTimeField(null=True)
    featured_image = models.CharField(max_length=400, null=True)

    # list pipelines by latest created
    class Meta:
        ordering = ['-date_created']

    # list pipelines by their name
    def __str__(self):
        return self.pipeline_name


# list of all results created for all pipelines
class Result(models.Model):

    pipeline_id = models.ForeignKey(List, on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    api_pipeline_id = models.CharField(max_length=100)
    output_id = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    message = models.CharField(max_length=100)
    interval_start_date = models.DateField()
    interval_end_date = models.DateField()
    
    # if an image is available for this result
    # null = True to allow for if no images are returned
    image_created_at = models.DateTimeField(null=True)
    image_updated_at = models.DateTimeField(null=True)
    image_previous_url = models.CharField(max_length=700, null=True)
    image_visual_url = models.CharField(max_length=700, null=True)
    image_analytics_url = models.CharField(max_length=700, null=True)
    image_metadata_url = models.CharField(max_length=700, null=True)
    image_size = models.CharField(max_length=10, null=True)
    image_valid_pixels_per = models.CharField(max_length=10, null=True)
    image_source = models.CharField(max_length=60, null=True)

    # image metadata
    scene_height = models.CharField(max_length=40, null=True)
    scene_width = models.CharField(max_length=40, null=True)
    filled_area = models.CharField(max_length=40, null=True)
    aoi_area_per = models.CharField(max_length=40, null=True)
    cloud_cover_per = models.CharField(max_length=40, null=True)
    aoi_cloud_cover_per = models.CharField(max_length=40, null=True)
    visible_area = models.CharField(max_length=40, null=True)
    aoi_visible_area_per = models.CharField(max_length=40, null=True)
