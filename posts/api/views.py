from rest_framework.response import Response
from rest_framework import generics
from ..models import Post
from . import serializers


class PostListView(generics.ListAPIView):
    """
    GET all posts from
    /api/posts/list/
    """

    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


