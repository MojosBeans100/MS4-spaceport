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

        widgets = {
            'pipeline_name': TextInput(attrs={
                'required': True,
                'class': 'form-control',
                'placeholder': 'eg. My First Pipeline',
                'id': 'pipeline_name',
                #'oninput': 'this.ClassName' = ''",
            }),
            'pipeline_des': Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Give your pipeline a unique description to identify it',
                'id': 'pipeline_des',
                #'oninput': 'this.ClassName' = ''",
            })
        }


class UpdateList(ModelForm):
    class Meta:
        model = List

        fields = ['pipeline_name', 'pipeline_des']

