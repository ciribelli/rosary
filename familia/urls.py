from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('rosario.urls')),
]
