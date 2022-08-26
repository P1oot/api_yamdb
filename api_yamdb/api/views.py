from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import PageNumberPagination

from .permissions import GetOrAdminOnly

from reviews.models import Category, Genre, Title
from .serializers import (
    CategorySerializer,
    GenreSerializer,
    TitleSerializer
)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (GetOrAdminOnly, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', )
    pagination_class = PageNumberPagination
    


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (GetOrAdminOnly, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', )
    pagination_class = PageNumberPagination


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    pagination_class = PageNumberPagination