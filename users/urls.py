from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    AddressViewSet,
    UserRegistrationAPIView,
    ProfileAPIView,
    SendOrResendSMSAPIView,
    UserAPIView,
    UserLoginAPIView,
    VerifyPhoneNumberAPIView,
)

app_name = 'users'

router = DefaultRouter()
router.register(r"", AddressViewSet)

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='user_register'),
    path('login/', UserLoginAPIView.as_view(), name='user_login'),
    path('send-sms/', SendOrResendSMSAPIView.as_view(), name='send_resend_sms'),
    path('verify/', VerifyPhoneNumberAPIView.as_view(), name='user_verify'),
    path('profile/', ProfileAPIView.as_view(), name='user_profile'),
    path('profile/address', include(router.urls)),
    path('', UserAPIView.as_view(), name='user')
]
