from django.forms import ModelForm

from my_music_app.accounts.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'