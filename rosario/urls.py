from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from . import views

app_name = 'rosario'
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    
]
