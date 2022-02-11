# Import 3rd party
import datetime

# Import django
from django.test import TestCase
from django.utils import timezone
import unittest
from unittest import mock

# Import local
from .models import List, Result
from .forms import CreateList, UpdateList


class TestViews(TestCase):

    def setUp(self):
        test_list = List.objects.create(
            pipeline_name='Test Pipeline',
            pipeline_des='Test description',
            start_date=datetime.date.today(),
            end_date=datetime.date.today(),
            output_image='1f0db8b2-b4d4-11e7-a775-a6fe70ce62b1',
            interval='1d',
            aoi={'json_field': 'json_object'},
            cloud_cover='10',
            created_by='test_user',
            # image_preview_url='www.image.com',
        )

        result = Result.objects.create(
            pipeline_id=test_list,
            created_at=timezone.now(),
            updated_at=timezone.now(),
            api_pipeline_id='',
            output_id='',
            status='',
            message='',
            interval_start_date=datetime.date.today(),
            interval_end_date=datetime.date.today()
        )

    def test_get_homepage(self):
        """
        views.homepage renders index.html
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_discover_page(self):
        """
        views.discover renders discover.html
        """
        response = self.client.get('/discover.html')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'discover.html')

    def test_get_user_models_page(self):
        """
        views.my_pipelines renders my_pipelines.html
        """
        response = self.client.get('/my_pipelines.html')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'my_pipelines.html')

    def test_detail_view_page(self):
        """
        views.detail_view renders detail_view/id
        """
        test_list = List.objects.get()

        response = self.client.get(f'/detail_view/{test_list.id}')
  
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['pipeline'], List)
        self.assertEquals(response.context['results'][0].pipeline_id, response.context['pipeline'])
        self.assertTemplateUsed(response, 'detail_view.html')

    def test_renders_delete_view(self):
        """
        renders the delete view
        with pipeline instance
        """

        test_list = List.objects.get()
        existing_result = Result.objects.filter(pipeline_id=test_list)
        response = self.client.get(f'/delete_view/{test_list.id}')

        # current num results is 1
        self.assertEqual(len(existing_result), 1)

        # context renders that pipeline instance
        self.assertIsInstance(response.context['pipeline'], List)

        # context renders correct List object
        self.assertEqual(response.context['pipeline'].id, test_list.id)

        # renders the correct template
        self.assertTemplateUsed(response, 'delete_view.html')

        # no error codes associated with rendering the template
        self.assertEqual(response.status_code, 200)

    def test_delete_conf(self):
        """
        test that the delete confirmation page is
        rendered then deletes the object in question
        """

        test_list = List.objects.get()

        response = self.client.get(f'/delete_conf/{test_list.id}')
        # self.assertRedirects(response, f'/delete_conf/{test_list.id}')

        existing_items = List.objects.filter(id=test_list.id)

        self.assertEqual(len(existing_items), 0)

    def test_get_edit_item_page(self):
        """
        test that the edit form is rendered
        with correct details
        """

        test_list = List.objects.get()

        response = self.client.get(f'/edit_pipeline/{test_list.id}')

        self.assertTemplateUsed(response, 'edit_pipeline.html')
        self.assertEqual(test_list.pipeline_name, response.context['form'].initial['pipeline_name'])
        self.assertEqual(test_list.pipeline_des, response.context['form'].initial['pipeline_des'])

    def test_can_edit_object(self):
        """
        test that users can edit details
        of a pipeline, and redirects back
        to the detail view
        """

        initial_object = List.objects.get()
        response = self.client.post(f'/edit_pipeline/{initial_object.id}', {'pipeline_name': 'Test name edited', 'pipeline_des': 'Test des edited'})
        edited_object = List.objects.get()

        self.assertRedirects(response, f'/detail_view/{initial_object.id}')
        self.assertEqual(edited_object.pipeline_name, 'Test name edited')
        self.assertEqual(edited_object.pipeline_des, 'Test des edited')

