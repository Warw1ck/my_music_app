from django.shortcuts import render, redirect

# Create your views here.
from my_music_app.accounts.models import Profile


def delete_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect('home page')

    context = {
        'profile': profile
    }
    return render(request, 'accounts/profile-delete.html', context=context)


def details_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {
        'profile': profile
    }
    return render(request, 'accounts/profile-details.html', context=context)