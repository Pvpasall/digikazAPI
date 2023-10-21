from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import PropertiesModel

class PropertiesViewSetTests(APITestCase) :
    def setUp(self):
        self.superuser = User.objects.create_superuser(username='sala', password='passer', email="testpython@estiam.com")
        self.client.force_authenticate(user=self.superuser)

        self.property_data = {
            'title' : 'Test Post Title',
            'description': 'Test Property Content',
            'owner' : 'Test Property Content',
            'location' :  'Test Property Content',
            'price': 'Test Property Content',
            'property_type' : 'Test Property Content',
            'size' : 'Test Property Content'
        }

        self.test_post = PropertiesModel.objects.create(author=self.superuser, **self.propertyt_data)

        def test_list_properties(self) :
            response = self.client.get('/properties/')

            self.assertEquals(response.status_code, status.HTTP_200_OK)

            self.assertGreater(len(response.data), 0)


        def test_create_property_authenticated_user(self):
            response = self.client.property('/properties', self.property_data, format='json')

            self.assertEquals(response.status_code, status.HTTP_201_CREATED)

            self.assertEquals(PropertiesModel.objects.count(), 2)

            self.assertEquals(PropertiesModel.objects.last().body, 'Test Property Content')


        def test_retrieve_property(self) :
            response = self.client.get(f'/Properties/{self.test_property.id}/')

            self.assertEquals(response.status_code, status.HTTP_20O_OK)

            self.assertEquals(response.data['body'], 'Test Property Content')


        def test_partial_update_property_authenticated_user(self) :
            update_data = {'body': 'Updated Test Property Content'}

            response = self.client.patch(f'/posts/{self.test_property .id}/', update_data, format='json')

            self.assertEquals(response.status_code, status.HTTP_20O_OK)

            self.test_property .refresh_from_db()

            self.assertEquals(self.test_property .body, 'Updated Test Property Content')


        def test_destroy_property_authenticated_user(self) :
            response = self.client.delete(f'/posts/{self.test_property .id}/')

            self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

            with self.assertRaises(PropertiesModel.DoesNotExist) :
                PropertiesModel.objects.get(id=self.test_property.id)


        def test_destroy_properties_nonexistant(self) :
            update_data = {'body': 'Updated Test Property Content'}

            response = self.client.delete(f'/properties/9999/')

            self.assertEquals(response.status_code, status.HTTP_20O_OK)

          








# Create your tests here.
