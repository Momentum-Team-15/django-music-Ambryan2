from re import A
from django.shortcuts import render, get_object_or_404
from .models import User, Album, Artist
from .forms import PostForm
from django.shortcuts import redirect
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    all_albums = Album.objects.all()
    person = User.objects.get(pk=1)
    # be able to filter by user id in objects
    return render(request, 'albums/index.html', {'albums': all_albums,'user': person})

def artist_shown(request):
    artist = Artist.objects.all()
    return render(request, 'albums/artist.html',{'artists':artist})

def post_detail(request, pk):
    post = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/post_detail.html', {'album': post})

def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    artist_album = Album.objects.filter(artist=pk)
    return render(request,'albums/artist_detail.html', {'artist':artist, 'artist_album':artist_album})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # this is save an instance of album in database. Commit=False is only needed if we need to add user
            album = form.save(commit=False)
            album.user = request.user
            album.created_at = timezone.now()
            album.save()
            return redirect('home') #, pk=album.pk)
    else:
        form = PostForm()
    return render(request, 'albums/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            album = form.save(commit=False)
            album.user = request.user
            album.created_at = timezone.now()
            album.save()
            return redirect('post_detail', pk=album.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'albums/post_edit.html', {'form': form})

def album_delete(request, pk):
    album = get_object_or_404(Album, pk=pk)
    # fetch the object related to passed id
    obj = get_object_or_404(Album, pk = pk)
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")
    return render(request, "albums/album_delete.html", {})
    

