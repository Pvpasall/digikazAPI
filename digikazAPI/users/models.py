from django.db import models

class User(models.Model):
    username = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    isloc = models.BooleanField(default=1) 

    # Ajoutez d'autres champs user au besoin
