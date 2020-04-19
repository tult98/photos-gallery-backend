from django.shortcuts import render
from .models import Photo
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework.decorators import api_view

# Create your views here.


def home(request):
    i = random.randint(0, 1001)
    photos = Photo.objects.all()[i:i+20]
    return render(request, 'index.html', {'photos': photos})


def photos(request):
    photos_list = Photo.objects.all()
    paginator = Paginator(photos_list, 30)
    page = request.GET.get('page') # get the page number
    photos = paginator.get_page(page)

    return render(request, 'photos.html', {'photos': photos})
