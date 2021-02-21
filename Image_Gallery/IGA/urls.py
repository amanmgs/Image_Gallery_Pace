from django.urls import path

from .views import *

urlpatterns = [
	path('image_upload', image_view, name = 'image_upload'),
	path('', display_images, name = 'display_images'),
]
