from django import forms

from .models import Album

class PostForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ('title', 'artist','favorite')
