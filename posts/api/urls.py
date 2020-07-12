from django.urls import path, re_path
from . import views

urlpatterns = [
    path('posts/list/', views.PostListView.as_view(), name=None),
    re_path(r'^posts/(?P<post_id>\d+)/likes_count', views.CountPostLikes().as_view(), name=None),
    re_path(r'^posts/(?P<post_id>\d+)/users_like', views.ListPostLikes().as_view(), name=None),
    re_path(r'^posts/(?P<post_id>\d+)/add_like', views.AddLike().as_view(), name=None),
    re_path(r'^posts/(?P<post_id>\d+)/unlike', views.RemoveLike().as_view(), name=None),
    path('posts/post_message/', views.MakePost().as_view()),
    path('posts/likes/list', views.LikeListView.as_view()),
    path('analitics/', views.DateCountLikes.as_view()),

]
