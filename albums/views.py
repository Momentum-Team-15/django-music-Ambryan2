from django.shortcuts import render
from .models import User, Album, Artist

# Create your views here.
def index(request):
    all_albums = Album.objects.all()
    person = User.objects.get(pk=1)
    return render(request, 'albums/index.html', {'all': all_albums,'user': person})




