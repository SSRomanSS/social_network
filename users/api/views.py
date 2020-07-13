from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
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


class CreateUserAPIView(APIView):
    """
    Allow any user (authenticated or not) to access this url
    Create new user
    """
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data

        email = data.get('email', None)
        password = data.get('password', None)
        user = CustomUser.objects.create_user(
            email=email,
            password=password)
        return Response(status=status.HTTP_200_OK)


class LoginUserAPIView(APIView):
    """
    Allow any user (authenticated or not) to access this url
    User login
    """

    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data

        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(email=email, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    """
    Allow only authenticated users to access this url
    Get users data, update users data
    """

    serializer_class = serializers.UserSerializer

    def get(self, request, *args, **kwargs):
        # serializer to handle turning our `User` object into something that
        # can be JSONified and sent to the client.
        serializer = self.serializer_class(request.user)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        serializer_data = request.data.get('user', {})

        serializer = serializers.UserSerializer(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)