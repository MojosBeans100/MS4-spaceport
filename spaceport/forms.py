from .models import List
from django.forms import ModelForm, DateInput, TextInput, Textarea, RadioSelect, Select

class CreateList(ModelForm):
    class Meta:
        model = List

        exclude = [
            'created_by',
            'date_created',
            'status',
            'api_id',
            'slug',
            'num_intervals',
            'num_results',
            'num_images',
            'results_updated',
            'featured_image'
        ]


class UpdateList(ModelForm):
    class Meta:
        model = List

        fields = ['pipeline_name', 'pipeline_des']
        