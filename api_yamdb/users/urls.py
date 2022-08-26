from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, AuthViewSet

app_name = 'users'

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('auth/signup', AuthViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
