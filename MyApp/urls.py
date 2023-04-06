from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('number/', views.evenodd),
    path('index/', views.index),
    path('variables/', views.variables),
    path('var2/', views.variable2),
    path('image1', views.images),
    path('', views.background),



]
