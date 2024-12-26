from django.shortcuts import render, redirect, get_object_or_404
from .models import Track


def home(request):
    return render(request, 'index.html')


def track_list(request):
    tracks = Track.objects.all()
    ctx = {'tracks': tracks}
    return render(request, 'tracks/music-list.html', ctx)


def track_create(request):
    if request.method == 'POST':
        music_title = request.POST.get('music_title')
        artist = request.POST.get('artist')
        album = request.POST.get('album')
        genre = request.POST.get('genre')
        release_date = request.POST.get('release_date')
        cover_image = request.FILES.get('cover_image')
        audio_file = request.FILES.get('audio_file')
        if music_title and artist and album and genre and release_date and cover_image and audio_file:
            Track.objects.create(
                music_title=music_title,
                artist=artist,
                album=album,
                genre=genre,
                release_date=release_date,
                cover_image=cover_image,
                audio_file=audio_file,
            )
            return redirect('home')
    return render(request, 'tracks/music-form.html')

def update(request, track_id):
    track = get_object_or_404(Track, pk=track_id)
    if request.method == 'POST':
        music_title = request.POST.get('music_title')
        artist = request.POST.get('artist')
        album = request.POST.get('album')
        genre = request.POST.get('genre')
        release_date = request.POST.get('release_date')
        cover_image = request.FILES.get('cover_image')
        audio_file = request.FILES.get('audio_file')
        if music_title and artist and album and genre and release_date and cover_image and audio_file:
            track.music_title = music_title
            track.artist = artist
            track.album = album
            track.genre = genre
            track.release_date = release_date
            track.cover_image = cover_image
            track.audio_file = audio_file
            track.save()
            return redirect(track.get_detail_url())
    ctx = {'track': track}
    return render(request, 'tracks/music-form.html', ctx)


def track_delete(request, track_id):
    track = get_object_or_404(Track, pk=track_id)
    track.delete()
    return redirect('tracks:list')

def detail(request, track_id):
    track = get_object_or_404(Track, pk=track_id)
    ctx = {'track': track}
    return render(request, 'tracks/music-detail.html', ctx)




