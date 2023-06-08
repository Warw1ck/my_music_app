from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('album/', include('my_music_app.album.urls')),
    path('profile/', include('my_music_app.accounts.urls')),
    path('', include('my_music_app.common.urls'),),
]
