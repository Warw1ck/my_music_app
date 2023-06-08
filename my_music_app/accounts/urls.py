from django.urls import path

from my_music_app.accounts.views import delete_profile, details_profile

urlpatterns = (
    path('delete/<int:pk>', delete_profile, name='delete profile'),
    path('details/<int:pk>', details_profile, name='details profile'),
)