from django.urls import path
from .views import register, login_user, logout_user, forgot_password
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('forgot-password/', forgot_password, name='forgot-password'),
    path('verify-email/<str:key>/', verify_email, name='verify-email'),
]
