from django.urls import path
from .views import RegistrationAPIView, LoginAPIView, LogoutAPIView

urlpatterns = [
    path('register/', RegistrationAPIView),
    path('login/', LoginAPIView),
    path('logout/', LogoutAPIView),
]