from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

from . import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import generics
from ..models import Post, Like
from . import serializers


class PostListView(generics.ListAPIView):
    """
    GET all posts from
    /api/posts/list/
    """

    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class LikeListView(generics.ListAPIView):
    """
    GET all posts from
    /api/posts/likes/list/
    """

    queryset = Like.objects.all()
    serializer_class = serializers.LikeSerializer


class CountPostLikes(APIView):
    """
    GET method for single post by unique identifier like counting
    /api/posts/<unique_message_identifier(Primary Key in a database)>/likes_count
    """

    def get(self, request, **kwargs):
        post_id = int(kwargs['post_id'])
        post = Post.objects.get(id=post_id).body
        like_count = Like.objects.all().filter(post_id=post_id).count()
        content = {post: f'has {like_count} likes'}
        return Response(content)


class ListPostLikes(generics.ListAPIView):
    """
    GET method for getting list of users who like single message by unique identifier
    /api/posts/<unique_message_identifier(Primary Key in a database)>/users_like
    """

    def get_queryset(self, **kwargs):
        post_id = int(self.kwargs['post_id'])
        queryset = Like.objects.all().filter(post_id=post_id)
        return queryset

    serializer_class = serializers.LikeSerializer


class MakePost(APIView):
    """
    POST method for creating a new post on
    /api/posts/post_message/
    """

    def post(self, request):
        if request.method == 'POST':

            serializer = serializers.PostSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddLike(APIView):
    """
    POST method for like a post
    /api/messages/<unique_message_identifier(Primary Key in a database)>/add_like
    """

    def post(self, request, **kwargs):
        if request.method == 'POST':
            data = {}
            data['post'] = int(kwargs['post_id'])
            data['user'] = request.user.id
            print(data)
            serializer = serializers.LikeSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
