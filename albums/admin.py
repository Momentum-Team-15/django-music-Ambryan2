from django.contrib import admin
from .models import Artist, User, Album

# Register your models here, so you can see them in admin
admin.site.register(User)
admin.site.register(Album)
admin.site.register(Artist)