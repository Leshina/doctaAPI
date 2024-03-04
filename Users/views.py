# auth/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login, logout
from allauth.account.views import SignupView, PasswordResetView, ConfirmEmailView

@api_view(['POST'])
def register(request):
    signup_view = SignupView.as_view()
    return signup_view(request)

@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def logout_user(request):
    logout(request)
    return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)

@api_view(['POST'])
def forgot_password(request):
    password_reset_view = PasswordResetView.as_view()
    return password_reset_view(request)

@api_view(['GET'])
def verify_email(request, key):
    confirm_email_view = ConfirmEmailView.as_view()
    return confirm_email_view(request._request, key=key)
