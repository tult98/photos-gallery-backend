from django.urls import path, re_path
from posts import views

urlpatterns = [
    path('categories/',
        views.CategoryList.as_view(),
        name=views.CategoryList.name
    ),
    re_path('categories/(?P<pk>[0-9]+)$',
        views.CategoryDetail.as_view(),
        name=views.CategoryDetail.name
    ),
    path('posts/',
        views.PostList.as_view(),
        name=views.PostList.name
    ),
    re_path('posts/(?P<pk>[0-9]+)$',
        views.PostDetail.as_view(),
        name=views.PostDetail.name
    ),
    path('tags/',
        views.TagList.as_view(),
        name=views.TagList.name
    ),
    re_path('tags/(?P<pk>[0-9]+)$',
        views.TagDetail.as_view(),
        name=views.TagDetail.name
    ),
    path('',
        views.ApiRoot.as_view(), 
        name=views.ApiRoot.name
    )
]