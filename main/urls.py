from django.contrib import admin
from django.urls import path
from .views import *

# 이미지 업로드
from django.conf.urls.static import static
from django.conf import settings

app_name = 'main'

urlpatterns = [
    path('', index),
    path('lost/', lost),
    path('foodtruck/', foodtruck),
    path('song-request/', songRequest),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)