from django.contrib import admin
from .models import List, Result


@admin.register(List)
class ListAdmin(admin.ModelAdmin):

    list_display = (
         'pipeline_name',
         'status',
         'created_by',
         'start_date',
         'end_date',
         'date_created',
         'cloud_cover',
         'num_results',
         'num_images',
    )

    admin.site.site_header = "Spaceport Pipelines Admin"
    list_filter = ('status', 'created_by')

    search_fields = ['pipeline_name']

    # class Meta:
    #     order_by('-created_at')



@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'pipeline_id',
        'status',
        'interval_start_date',
        'interval_end_date',
    )
