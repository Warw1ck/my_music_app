from django.forms import ModelForm

from my_music_app.album.models import Album


class BaseAlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = '__all__'


class AlbumAddForm(BaseAlbumForm):
    pass


class AlbumEditForm(BaseAlbumForm):
    pass


class AlbumDeleteForm(BaseAlbumForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
            field.widget.attrs['disable'] = 'disable'