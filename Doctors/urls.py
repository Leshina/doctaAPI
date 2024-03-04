from django.urls import path
from .views import doctor_list, doctor_detail, search_doctor

urlpatterns = [
    path('', doctor_list, name='doctor-list'),
    path('<uuid:pk>', doctor_detail, name='doctor-detail'),
    path('search', search_doctor, name='search-doctor'),
]
