from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, UserAuthSerializer


# Create your views here.
@api_view(http_method_names=['POST'])
def RegistrationAPIView(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(http_method_names=['POST'])
def LoginAPIView(request):
    if request.method == 'POST':
        serializer = UserAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({"key": token.key}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(http_method_names=['POST'])
def LogoutAPIView(request):
    if request.method == 'POST':
        logout(request)
        return Response({"message": "User logged out successfully"}, status=status.HTTP_200_OK)
    return Response({"error": "Invalid request"}, status=status.HTTP_400_BAD_REQUEST)