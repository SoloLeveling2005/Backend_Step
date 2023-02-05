from django.conf import settings
from django.urls import path, re_path
from django_app import views
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index, name="index"),
    path('todo/', views.index, name="index"),
    # path('posts/<id:int>', views.index, name="posts"),
    # path('posts/<id:int>/comment', views.index, name="posts"),

    # re_path(r'^posts/$', views.posts, name="posts"),
    # re_path(r'^posts/(?P<id>\d+)/$', views.posts_one, name="posts_one"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
