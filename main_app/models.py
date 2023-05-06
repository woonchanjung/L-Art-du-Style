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
