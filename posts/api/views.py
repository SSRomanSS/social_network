from datetime import datetime, timedelta
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from . import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import generics
from django.db.models import Count
from django.db.models.functions import TruncDate
from ..models import Post, Like
from . import serializers


class PostListView(generics.ListAPIView):
    """
    GET all posts from
    /api/posts/list/
    """

    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [AllowAny, ]


class LikeListView(generics.ListAPIView):
    """
    GET all posts from
    /api/posts/likes/list/
    """

    queryset = Like.objects.all()
    serializer_class = serializers.LikeSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly, ]

class CountPostLikes(APIView):
    """
    GET method for single post by unique identifier like counting
    /api/posts/<unique_message_identifier(Primary Key in a database)>/likes_count
    """

    def get(self, request, **kwargs):
        post_id = int(kwargs['post_id'])
        post = Post.objects.get(id=post_id).body
        like_count = Like.objects.filter(post_id=post_id).count()
        content = {post: f'has {like_count} likes'}
        return Response(content)


class DateCountLikes(APIView):
    """
    GET method for like counting by date
    api/analitics/?date_from=<yyyy-mm-dd>&date_to=<yyyy-mm-dd>
    """

    def get(self, request):

        date_from = datetime.strptime(request.GET.get('date_from'), "%Y-%m-%d")
        date_to = datetime.strptime(request.GET.get('date_to'), "%Y-%m-%d") + timedelta(days=1)
        likes = Like.objects. \
            extra({'time': "date_trunc('day', time)"}).\
            filter(time__range=(date_from, date_to)).\
            values('time__date').\
            annotate(total_like=Count('id'))  # extra expression working with PostgreSQL
            # annotate(time=TruncDate('time'))  # working universal
        return Response(likes)


class ListPostLikes(generics.ListAPIView):
    """
    GET method for getting list of users who like single message by unique identifier
    /api/posts/<unique_message_identifier(Primary Key in a database)>/users_like
    """

    def get_queryset(self, **kwargs):
        post_id = int(self.kwargs['post_id'])
        queryset = Like.objects.filter(post_id=post_id)
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
    /api/posts/<unique_message_identifier(Primary Key in a database)>/add_like
    """

    def post(self, request, **kwargs):
        if request.method == 'POST':
            data = {}
            post_id = int(kwargs['post_id'])
            user_id = request.user.id
            data['post'] = post_id
            data['user'] = user_id
            if not Like.objects.filter(post=post_id, user=user_id).exists():
                serializer = serializers.LikeSerializer(data=data)

                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return Response({f'post {post_id}': 'is already liked'})


class RemoveLike(APIView):
    """
     POST method for unlike a post
    /api/posts/<unique_message_identifier(Primary Key in a database)>/unlike
    """
    def post(self, request, **kwargs):
        if request.method == 'POST':
            post_id = int(kwargs['post_id'])
            user_id = request.user.id
            like = Like.objects.filter(post=post_id, user=user_id)
            if like.exists():
                like.delete()
                return Response({f'post {post_id}': 'is unliked'})
            return Response({f'post {post_id}': f'is not liked yet by {user_id}'})
