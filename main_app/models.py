from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Top(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to='tops/')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Top #{self.pk}"

class Bottom(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    image = models.ImageField(upload_to='bottoms/')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Bottom #{self.pk}"

class Match(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    tops = models.ManyToManyField(Top)
    bottoms = models.ManyToManyField(Bottom)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Match #{self.pk}"