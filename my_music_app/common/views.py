from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render

# Create your views here.
from my_music_app.accounts.forms import ProfileForm
from my_music_app.accounts.models import Profile
from my_music_app.album.models import Album


def check_for_user():
    try:
        return Profile.objects.get()
    except:
        return None


def home_page(request):
    if not check_for_user():
        form = ProfileForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home page')
        context = {
            'form': form
        }
        return render(request, 'common/home-no-profile.html', context=context)
    albums = Album.objects.all()
    context = {
        'albums': albums

    }

    return render(request, 'common/home-with-profile.html', context=context)