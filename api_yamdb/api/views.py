from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from reviews.models import Category, Genre, Review, Title

from .permissions import GetOrAdminOnly
from .serializers import (CategorySerializer, CommentSerializer,
                          GenreSerializer, GetTitleSerializer, ReviewSerializer,
                          TitleSerializer)


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
    permission_classes = (GetOrAdminOnly, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', )

    def get_serializer_class(self):
        if self.action == 'list':
            return GetTitleSerializer
        if self.action == 'retrieve':
            return GetTitleSerializer
        return TitleSerializer



class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        review = get_object_or_404(Review, id=self.kwargs.get('review_id'))
        return review.comments.all()

    def perform_create(self, serializer):
        review = get_object_or_404(Review, id=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review=review)
