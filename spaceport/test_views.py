from django.test import TestCase
from .models import List, Result

class TestViews(TestCase):

    def setUp(self):
        test_list = List.objects.create(
            pipeline_name='Test Pipeline',
            pipeline_des='Test description',
            start_date='2022-01-23',
            end_date='2022-01-28',
            output_image='1f0db8b2-b4d4-11e7-a775-a6fe70ce62b1',
            interval='1d',
            aoi={'json_field': 'json_object'},
            cloud_cover='10',
            created_by='test_user',
            # image_preview_url='www.image.com',
        )

        result = Result.objects.create(
            pipeline_id=test_list,
            created_at='2022-01-23 16:15',
            updated_at='2022-01-23 16:15',
            api_pipeline_id='',
            output_id='',
            status='',
            message='',
            interval_start_date='2022-01-23',
            interval_end_date='2022-01-23'
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

    def test_get_api_page(self):
        """
        views.api_error renders api_error.html
        """
        response = self.client.get('/api_error.html')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'api_error.html')

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

    def test_delete_view(self):

        test_list = List.objects.get()
        response = self.client.get(f'/delete_view/{test_list.id}')

        self.assertIsInstance(response.context['pipeline'], List)
        self.assertEqual(response.context['pipeline'].id, test_list.id)
        self.assertTemplateUsed(response, 'delete_view.html')
        self.assertEqual(response.status_code, 200)
        
    # def test_delete(self):

