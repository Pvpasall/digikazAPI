from django.db import models
from django.contrib.auth.models import User


def get_default_author():
    user = User.objects.get_or_create(username="admin")[0]
    return user.id


class PropertiesModel(models.Model):
    TYPE_CHOICES = (
        ("house", "House"),
        ("apartment", "Apartment"),
        ("studio", "Studio"),
    )

    title = models.CharField(max_length=150)
    description = models.TextField()
    userId = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="properties",
        default=get_default_author,
    )
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    property_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    size = models.PositiveIntegerField()

    def str(self):
        return self.title
