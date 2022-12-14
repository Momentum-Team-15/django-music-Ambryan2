from tkinter import CASCADE
from turtle import title
from unicodedata import name
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Album(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE, null=True )
    title = models.CharField(max_length=200)
    artist =  models.ForeignKey('Artist', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    favorite = models.BooleanField(null=True)

    def __str__(self):
        return f"{self.title} by {self.artist}"

class Artist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name