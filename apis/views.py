from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView, 
    DestroyAPIView,
    RetrieveAPIView, 
)
from photos.models import Photo
from rest_framework.response import Response
from .serializers import PhotoDetailSerialize, PhotoListSeriaLize


# Create your views here.

class PhotoListAPIView(ListAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoListSeriaLize


class PhotoDetailAPIView(RetrieveAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoDetailSerialize

class PhotoCreateAPIView(CreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoDetailSerialize

class PhotoUpdateAPIView(UpdateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoDetailSerialize

class PhotoDeleteAPIView(DestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoDetailSerialize

