from .models import List, output, status_choice
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
            'featured_image',
            'time_edited',
            #'aoi_area',
        ]

        widgets = {
            'pipeline_name': TextInput(attrs={
                'required': True,
                'class': 'form-control',
                'placeholder': 'eg. My First Pipeline',
                'id': 'pipeline_name',
                'oninput': "this.className = ''",
            }),
            'pipeline_des': Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Give your pipeline a unique description to identify it',
                'id': 'pipeline_des',
                'oninput': "this.className = ''",
            }),
            'aoi': TextInput(attrs={
                'required': True,
                'class': 'form-control',
                'id': 'id_aoi',
                'oninput': "this.className = ''",
            }),
            'start_date': DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'id': 'start_date',
                'placeholder': 'Start date', 'type': 'text',
                'onfocus': "(this.type='date')",
                'onChange': 'validateDate()',
                'oninput': "this.className = ''",
            }),
            'end_date': DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'id': 'end_date',
                'placeholder': 'End date', 'type': 'text',
                'onfocus': "(this.type='date')",
                'onChange': 'validateDate()',
                'oninput': "this.className = ''",
            }),
            'interval': Select(attrs={
                'class': 'form-control',
                'id': 'interval',
                'onChange': 'validateDate()',
                'oninput': "this.className = ''",
            }),
            'output_image': RadioSelect(choices='output_image', attrs={
                #'class': 'form-control',
                'id': 'id_output',
                'onchange': 'styleOutputImage()',
                'oninput': "this.className = ''",
            })
        }


class UpdateList(ModelForm):
    class Meta:
        model = List

        fields = ['pipeline_name', 'pipeline_des']

        widgets = {
            'pipeline_name': TextInput(attrs={
                'class': 'form-control',
                'id': 'pipeline_name',
            }),
            'pipeline_des': Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'id': 'pipeline_des',
            }),
            # 'status': RadioSelect(choices='status_choice', attrs={
            #     #'class': 'form-control',
                
            # }),
        }

