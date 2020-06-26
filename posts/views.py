from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.reverse import reverse
from django.core.exceptions import (
    ValidationError
)
# libraries for grated permissions 
from rest_framework import permissions
from posts import custompermission
from rest_framework.authentication import TokenAuthentication
from posts.models import (
    Category, 
    Tag, 
    Post
)
from django.contrib.auth.models import User
from posts.serializers import (
    CategotySerializer,
    TagSerializer, 
    PostSerializer
)

# Create your views here.

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all() 
    serializer_class = CategotySerializer
    name = 'category-list'
    permission_classes = (
        permissions.IsAdminUser,
    )
          

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all() 
    serializer_class = CategotySerializer
    name = 'category-detail'
    permission_classes = (
        custompermission.IsAdminOrReadOnly,
    )

class TagList(generics.ListCreateAPIView):
    queryset= Tag.objects.all() 
    serializer_class = TagSerializer
    name = 'tag-list'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

    @staticmethod
    def check_tag(data): 
        tag = Tag.objects.all().filter(name=data['name'])
        if tag:
            return True
        return False

    def create(self, request, *args, **kwargs): 
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if self.check_tag(request.data) == False: 
            self.perform_create(serializer)
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            data={'name': 'tag with this name already exists.'},
            status=status.HTTP_400_BAD_REQUEST
        )

    


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= Tag.objects.all() 
    serializer_class = TagSerializer
    name = 'tag-detail'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custompermission.IsAdminOrReadOnly,
    )


class PostList(generics.ListCreateAPIView):
    queryset= Post.objects.all() 
    serializer_class = PostSerializer
    name = 'post-list'
    permission_classes = ( 
        permissions.IsAuthenticatedOrReadOnly,
    )   

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= Post.objects.all() 
    serializer_class = PostSerializer
    name = 'post-detail'
    permission_classes = (
        custompermission.IsAuthorOrReadOnly,
    )

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'categories': reverse(CategoryList.name, request=request),
            'posts': reverse(PostList.name, request=request),
            'tags': reverse(TagList.name, request=request),
        })