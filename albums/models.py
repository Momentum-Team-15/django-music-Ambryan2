from turtle import title
from unittest.util import _MAX_LENGTH
from django.conf import settings
from django.db import models
# from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist =  models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.artist}"