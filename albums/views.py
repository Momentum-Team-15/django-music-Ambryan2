from django.shortcuts import render

# Create your views here.
def album_directory(request):
    return render(request, 'homescreen.html', {})