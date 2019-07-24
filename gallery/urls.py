from django.urls import path
from . import views

urlpatterns = [
    path('', views.PhotosList.as_view(), name='photos'),
]
