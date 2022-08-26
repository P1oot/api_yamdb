from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, UserCreateViewSet, TokenViewSet

app_name = 'users'

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('auth/signup', UserCreateViewSet)
router.register('auth/token', TokenViewSet, basename='token')

urlpatterns = [
    path('', include(router.urls)),
]
