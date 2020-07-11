from rest_framework import generics
from .. models import CustomUser
from . import serializers


class UserListView(generics.ListAPIView):
    """
    GET all users from
    /api/users/list/
    """

    queryset = CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
