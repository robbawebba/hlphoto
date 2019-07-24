from django.urls import path
from . import views

urlpatterns = [
    path('', views.PhotosList.as_view(), name='photos'),
    path('photo/<int:key>/order/', views.OrderPrints, name='order-prints'),
]
