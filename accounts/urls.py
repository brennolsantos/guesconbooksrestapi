from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework import routers
from .views import RegisterView, CheckView, UpdateProfileView

app_name = 'accounts'

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'register', RegisterView, basename='register')
router.register(r'check/', CheckView, basename='check')
router.register(r'update', UpdateProfileView, basename='update')

urlpatterns = [
    path('token-auth', obtain_jwt_token),
    path('token-refresh', refresh_jwt_token),
    path('', include(router.urls))
]
