from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name =  models.CharField(max_length=50)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
