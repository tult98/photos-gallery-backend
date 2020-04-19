from rest_framework import serializers
from photos.models import Photo

class PhotoDetailSerialize(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = "__all__"

class PhotoListSeriaLize(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'url')
        
