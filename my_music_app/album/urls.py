from django.urls import path

from my_music_app.album.views import add_album, details_album, edit_album, delete_album

urlpatterns = (
    path('add', add_album, name='add album'),
    path('details/<int:pk>', details_album, name='details album'),
    path('edit/<int:pk>', edit_album, name='edit album'),
    path('delete/<int:pk>', delete_album, name='delete album'),

)