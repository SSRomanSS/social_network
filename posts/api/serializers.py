from rest_framework import serializers
from ..models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for Post Model
    """
    class Meta:
        model = Post
        fields = ('author',
                  'body',
                  'date_published')


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for Like Model
    """

    class Meta:
        model = Like
        fields = ('post',
                  'user',
                  'time',)


