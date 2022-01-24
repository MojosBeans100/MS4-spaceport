from django.test import TestCase

class TestViews(TestCase):

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
