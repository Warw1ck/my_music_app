from django.shortcuts import render, redirect

from my_music_app.album.models import Album
from my_music_app.common.forms import AlbumAddForm, AlbumEditForm, AlbumDeleteForm


def add_album(request):
    form = AlbumAddForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home page')
    context = {
        'form': form
    }
    return render(request, 'album/add-album.html', context=context)


def details_album(request, pk):
    album = Album.objects.get(id=pk)
    context = {
        'album': album
    }
    return render(request, 'album/album-details.html', context=context)


def edit_album(request, pk):
    album = Album.objects.get(id=pk)
    if request.method == 'GET':
        form = AlbumEditForm(instance=album)
    else:
        form = AlbumEditForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('details album', pk)

    context = {
        'form': form
    }
    return render(request, 'album/edit-album.html', context=context)


def delete_album(request, pk):
    album = Album.objects.get(id=pk)
    if request.method == 'POST':
        album.delete()
        return redirect('home page')
    form = AlbumDeleteForm(initial=album.__dict__)
    context = {
        'form': form
    }
    return render(request, 'album/delete-album.html', context=context)