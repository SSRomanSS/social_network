from django.urls import path, re_path
from . import views

urlpatterns = [
    path('users/list/', views.UserListView.as_view(), name=None),
    path('user/create/', views.CreateUserAPIView.as_view(), name=None),
    path('user/login/', views.LoginUserAPIView.as_view(), name=None),
    path('user/update/', views.UserRetrieveUpdateAPIView.as_view(), name=None),

]
