from django.shortcuts import get_object_or_404
from .models import User
from .serializers import UserSerializer, UserEditSerializer
from rest_framework import viewsets, mixins, permissions, status
from .permissions import Admin
from rest_framework.decorators import action
from rest_framework.response import Response


class RetriveUpdateViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    pass


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [Admin]

    @action(
        methods=['get', 'patch'],
        detail=False,
        url_path='me',
        url_name='me',
        permission_classes=[permissions.IsAuthenticated],
        serializer_class=UserEditSerializer,
    )
    def user_own_profile(self, request):
        user = get_object_or_404(User, username=request.user)
        serializer = self.get_serializer(user, data=request.data,
                                         partial=True)
        serializer.is_valid(raise_exception=True)
        if request.method == 'PATCH':
            serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
