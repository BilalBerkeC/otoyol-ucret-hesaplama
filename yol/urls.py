from django.contrib import admin
from django.urls import path
from yol import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('sorgula/', views.sorgula, name='sorgula'),
]