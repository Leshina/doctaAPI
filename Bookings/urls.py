from django.urls import path
from .views import bookings_list, bookings_detail

urlpatterns = [
    path('', bookings_list, name='bookings-list'),
    path('<int:pk>', bookings_detail, name='bookings-detail'),
]
