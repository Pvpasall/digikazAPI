from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import PropertiesModel


class PropertiesViewSetTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="usertest",
            password="passer",
        )
        self.client.force_authenticate(user=self.user)

        self.property_data = {
            "title": "Test Post Title",
            "description": "Test Property Content",
            # "userId": self.user,
            "location": "Test Property Content",
            "price": 1000,
            "property_type": "Test Property Content",
            "size": 200,
        }

        self.test_property = PropertiesModel.objects.create(**self.property_data)

    def test_list_properties(self):
        response = self.client.get("/properties/")

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertGreater(len(response.data), 0)

    def test_create_property_authenticated_user(self):
        response = self.client.post("/properties", self.property_data, format="json")

        self.assertEquals(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

        self.assertEquals(PropertiesModel.objects.count(), 1)
        print(PropertiesModel.objects.count(), 1)

        self.assertEquals(PropertiesModel.objects.last().size, 200)

    def test_retrieve_property(self):
        response = self.client.get(f"/properties/{self.test_property.id}/")

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.assertEquals(response.data["description"], "Test Property Content")

    def test_partial_update_property_authenticated_user(self):
        update_data = {"description": "Updated Test Property Content"}

        response = self.client.patch(
            f"/properties/{self.test_property.id}/", update_data, format="json"
        )

        self.assertEquals(response.status_code, status.HTTP_200_OK)

        self.test_property.refresh_from_db()

        self.assertEquals(
            self.test_property.description, "Updated Test Property Content"
        )

    def test_destroy_property_authenticated_user(self):
        response = self.client.delete(f"/properties/{self.test_property.id}/")

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(PropertiesModel.DoesNotExist):
            PropertiesModel.objects.get(id=self.test_property.id)

    def test_destroy_properties_nonexistent(self):
        response = self.client.delete(f"/properties/9999/")

        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)
