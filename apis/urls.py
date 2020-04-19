from django.urls import path, include, re_path
from .views import (
    PhotoDetailAPIView,
    PhotoListAPIView, 
    PhotoUpdateAPIView,
    PhotoDeleteAPIView, 
    PhotoCreateAPIView
)

urlpatterns = [
    path('photos/', PhotoListAPIView.as_view(), name='list'),
    path('photos/create/', PhotoCreateAPIView.as_view(), name='create'),
    re_path('photos/(?P<pk>\d+)/detail/', PhotoDetailAPIView.as_view(), name='detail'),
    re_path('photos/(?P<pk>\d+)/update/', PhotoUpdateAPIView.as_view(), name='update'),
    re_path('photos/(?P<pk>\d+)/delete/', PhotoDeleteAPIView.as_view(), name='delete'),
]   