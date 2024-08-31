from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('track/', views.track, name='track'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landingpage.urls')),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
