from django.shortcuts import render, get_object_or_404
from .models import User, Album, Artist
from .forms import PostForm
from django.shortcuts import redirect
from django.utils import timezone

# Create your views here.
def index(request):
    all_albums = Album.objects.all()
    person = Album.objects.get(pk=1)
    # be able to filter by user id in objects
    return render(request, 'albums/index.html', {'albums': all_albums,'user': person})

def post_detail(request, pk):
    post = get_object_or_404(Album, pk=pk)
    return render(request, 'albums/post_detail.html', {'album': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.author = request.user
            album.created_at = timezone.now()
            album.save()
            return redirect('post_detail', pk=album.pk)
    else:
        form = PostForm()
    return render(request, 'albums/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            album = form.save(commit=False)
            album.author = request.user
            album.created_at = timezone.now()
            album.save()
            return redirect('post_detail', pk=album.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'albums/post_edit.html', {'form': form})

