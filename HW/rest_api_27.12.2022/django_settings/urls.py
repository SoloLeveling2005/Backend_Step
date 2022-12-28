
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),



    path('api/', include('django_api.urls')),

    path('api-auth/', include('rest_framework.urls'))
]
