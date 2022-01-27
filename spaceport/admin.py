from django.contrib import admin
from .models import List, Result


@admin.register(List)
class ListAdmin(admin.ModelAdmin):
    list_display = (
         'id',
         'pipeline_name',
         'created_by',
         'start_date',
         'end_date',
         'date_created',
         'cloud_cover',
    )

    # prepopulated_fields = {'slug': ('pipeline_name',)}


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'pipeline_id',
        'status',
        'interval_start_date',
        'interval_end_date',
    )
