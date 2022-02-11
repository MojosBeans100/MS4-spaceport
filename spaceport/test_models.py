from django.contrib.auth.models import User
from django.test import TestCase
from .models import List

class TestListModel(TestCase):
    """
    A class for testing the List model
    """

    def setUp(self):

        test_user = User.objects.create_user(
            username='test_user',
            password='test_password'
        )

        test_list = List.objects.create(
            pipeline_name='Test Pipeline',
            pipeline_des='Test description',
            start_date='2022-01-23',
            end_date='2022-01-28',
            output_image='1f0db8b2-b4d4-11e7-a775-a6fe70ce62b1',
            interval='1d',
            aoi={'json_field': 'json_object'},
            cloud_cover='10',
        )

    def tearDown(self):
        """
        Delete list
        """
        List.objects.all().delete()

    def test_list_str_method(self):
        """
        Test the List str method
        """
        list = List.objects.get()
        self.assertEqual((list.__str__()), "Test Pipeline")
