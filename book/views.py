from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from .serializers import (
    BookSerializer,
    RecommendationSerializer,
    CommentSerializer,
    LikeSerializer,
)
from .models import Book, Recommendation, Comment, Like


@extend_schema(
    tags=["Books"],
)
class BookViewsets(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()


@extend_schema(
    tags=["Recommendations"],
)
class RecommendationViewsets(viewsets.ModelViewSet):
    serializer_class = RecommendationSerializer
    permission_classes = [IsAuthenticated]
    queryset = Recommendation.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = {
        'created_at': ['exact', 'gte', 'lte'],
        'book__genre': ['exact'],
        'book__rating': ['exact', 'gte', 'lte'],
    }
    ordering_fields = ['created_at', 'book__genre', 'book__rating']


@extend_schema(
    tags=["Comments"],
)
class CommentViewsets(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()


@extend_schema(
    tags=["Likes"],
)
class LikeViewsets(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]
    queryset = Like.objects.all()


@extend_schema(
    tags=["google-books-library"],
)
class GoogleBookViewsets(generics.ListAPIView):
    
    def list(self, request):
        pass