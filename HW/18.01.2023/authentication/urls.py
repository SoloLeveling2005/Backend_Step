from django.urls import path, re_path
from authentication import views


app_name = 'authentication'
urlpatterns = [
    path('', views.index, name="index"),

    # re_path(r'^auth/$', views.tasks, name="tasks"),
    # re_path(r'^user/(?P<user_id>\d+)/$', views.index, name="index"),



    # # TODO rest-api маршруты
    # path('todos_native/', views.todos_native),
    # path('todos_native/<int:pk>/', views.todos_native),
    #
    # re_path(r'^todos_drf/$', views.todos_drf),
    # re_path(r'^todos_drf/(?P<pk>\d+)/$', views.todos_drf),
]