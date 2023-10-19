from django.db import models



class PropertiesModel(models.Model) :    

    TYPE_CHOICES = (
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('studio', 'Studio'),
       
    )

    title = models.CharField(max_length=150)
    description = models.TextField()
    owner = models.CharField(max_length=150)
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    property_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    size = models.PositiveIntegerField()  


    def str (self) :
        return self.title
    