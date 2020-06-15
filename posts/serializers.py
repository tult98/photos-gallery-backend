from rest_framework import serializers
from posts.models import (
    Category,
    Tag, 
    Post
)
from django.contrib.auth.models import User
from django.core import validators

import posts.views


class CategotySerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='post-detail'
    )

    class Meta:
        model = Category
        fields = (
            'url', 
            'pk',
            'name', 
            'posts',
            'created_at',
            'updated_at',
        )

# class AuthorSerializer(serializers.HyperlinkedModelSerializer):
#     posts =  serializers.HyperlinkedRelatedField(
#         many=True,
#         read_only=True, 
#         view_name='post-detail',
#     )
#     gender = serializers.ChoiceField(
#         choices=Author.GENDER_CHOICES
#     )
#     gender_description = serializers.CharField(
#         source='get_gender_display',
#         read_only=True
#     )

#     class Meta:
#         model = Author
#         fields = (
#             'url', 
#             'pk', 
#             'username', 
#             'full_name', 
#             'gender',
#             'gender_description',
#             'posts_count',
#             'posts',
#             'created_at', 
#             'updated_at',
#         )

class TagSerializer(serializers.HyperlinkedModelSerializer): 
    posts = serializers.HyperlinkedRelatedField(
        many=True, 
        read_only=True, 
        view_name='post-detail'
    )

    class Meta:
        model = Tag
        fields = (
            'url', 
            'pk',
            'name', 
            'posts', 
            'created_at', 
            'updated_at',
        )

class PostTagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Tag
        fields = (
            'url', 
            'name'
        )

class UserPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = (
            'url',
            'title'
        )

class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = UserPostSerializer(
        many=True,
        read_only=True
    )

    class Meta: 
        model = User
        fields = (
            'url',
            'pk',
            'username', 
            'posts',
        )


class PostSerializer(serializers.HyperlinkedModelSerializer):
    # display the category name 
    category = serializers.SlugRelatedField(queryset=Category.objects.all(), slug_field='name')
    author = serializers.ReadOnlyField(source='author.username')
    tags = PostTagSerializer(many=True, required=False)
    class Meta:
        model = Post
        fields = (
            'url',
            'pk', 
            'category',
            'author',
            'tags',
            'title',
            # 'image',
            'content',
            'created_at',
            'updated_at',
        )
    
    # this method for modify data before validation step
    def to_internal_value(self, data):
        try:
            tags_data = data['tags']
        except:
            tags_data = []
        finally:
            tags = []
            for tag_data in tags_data:
                tag = {'name': tag_data}
                tags.append(tag)
            data['tags'] = tags
            return super().to_internal_value(data)

    @staticmethod
    def add_tags_to_post(obj, tags_data):
        for tag_data in tags_data: 
            if len(Tag.objects.all().filter(name=tag_data['name'])) > 0:
                tag = Tag.objects.all().filter(name=tag_data['name'])[0]
                tag.posts.add(obj)
            else: 
                tag = Tag.objects.create(name=tag_data['name'])
                tag.posts.add(obj)

    def create(self, validated_data):
        try:
            tags_data = validated_data.pop('tags')
        except:
            tags_data = []
        finally:
            post = Post.objects.create(**validated_data)
            self.add_tags_to_post(post, tags_data)
            return post

    def update(self, instance, validated_data):
        try:
            tags_data = validated_data.pop('tags')
        except: 
            tags_data = []
        finally:
            instance.title = validated_data.get('title', instance.title)
            instance.content = validated_data.get('content', instance.content)
            instance.category = validated_data.get('category', instance.category)
            instance.author = validated_data.get('author', instance.author)
            self.add_tags_to_post(instance, tags_data)
            instance.save()
            return instance
    
