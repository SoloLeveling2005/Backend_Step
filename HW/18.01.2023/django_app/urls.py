
from django.urls import path, re_path
from django_app import views


app_name = 'django_app'
urlpatterns = [
    path('', views.index, name="tasks"),

    # re_path(r'^tasks/$', views.tasks, name="tasks"),
    # re_path(r'^tasks/(?P<id>\d+)/$', views.tasks, name="task"),



    # # TODO rest-api маршруты
    # path('todos_native/', views.todos_native),
    # path('todos_native/<int:pk>/', views.todos_native),
    #
    # re_path(r'^todos_drf/$', views.todos_drf),
    # re_path(r'^todos_drf/(?P<pk>\d+)/$', views.todos_drf),
]