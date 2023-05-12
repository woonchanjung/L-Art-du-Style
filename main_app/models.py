from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Top(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='tops/')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} Top #{self.pk}"


class Bottom(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='bottoms/')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name} Bottom #{self.pk}"


class Match(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    top = models.ForeignKey(Top, on_delete=models.CASCADE, null=True)
    bottom = models.ForeignKey(Bottom, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Match #{self.pk}"