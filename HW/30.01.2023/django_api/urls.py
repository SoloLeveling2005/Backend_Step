
from django.urls import path, re_path
from django_api import views

urlpatterns = [
    path('', views.index, name="index"),
    # path('posts/', views.index, name="posts"),
    # path('posts/<id:int>', views.index, name="posts"),
    # path('posts/<id:int>/comment', views.index, name="posts"),

    # re_path(r'^posts/$', views.posts, name="posts"),
    # re_path(r'^posts/(?P<id>\d+)/$', views.posts_one, name="posts_one"),

]
