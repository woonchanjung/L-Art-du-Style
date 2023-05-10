from django.db import models
from django.urls import reverse
from datetime import date
# Import the User
from django.contrib.auth.models import User

# class Photo(models.Model):
#     url = models.CharField(max_length=200)
#     cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"Photo for cat_id: {self.cat_id} @{self.url}"

class Top(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='top_images/')
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Bottom(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='bottom_images/')
    color = models.CharField(max_length=50)

    def __str__(self):
        return self.name