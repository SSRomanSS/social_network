from rest_framework import serializers
from ..models import Post


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for Message Model
    """
    class Meta:
        model = Post
        fields = ('author', 'body', 'date_published')
