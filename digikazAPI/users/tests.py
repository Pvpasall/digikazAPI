from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", email="testuser@example.com", password="testpassword"
        )

    def test_create_user(self):
        """Test creating a new user with the custom user model."""
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "testuser@example.com")
        self.assertTrue(self.user.check_password("testpassword"))

    def test_create_superuser(self):
        """Test creating a new superuser with the custom user model."""
        admin_user = get_user_model().objects.create_superuser(
            username="adminuser",
            email="adminuser@example.com",
            password="adminpassword",
        )

        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

    def test_user_str(self):
        """Test the user string representation."""
        self.assertEqual(str(self.user), "testuser")
