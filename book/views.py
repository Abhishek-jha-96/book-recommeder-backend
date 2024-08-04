import requests

from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.response import Response


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
        "created_at": ["exact", "gte", "lte"],
        "book__genre": ["exact"],
        "book__rating": ["exact", "gte", "lte"],
    }
    ordering_fields = ["created_at", "book__genre", "book__rating"]


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
    parameters=[
        OpenApiParameter(
            name='q',
            description='Search query for books. Can be a keyword, author, or category.',
            required=True,
            type=OpenApiTypes.STR
        ),
    ]
)
class GoogleBookView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def list(self, request):
        query = request.GET.get("q")
        if not query:
            return Response(
                {"error": "A query parameter 'q' is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            response = requests.get(
                "https://www.googleapis.com/books/v1/volumes", params={"q": query}
            )
            response.raise_for_status()
            data = response.json()

            books = []
            for item in data.get("items", []):
                volume_info = item.get("volumeInfo", {})
                book = {
                    "title": volume_info.get("title"),
                    "authors": volume_info.get("authors", []),
                    "description": volume_info.get("description"),
                    "cover_image": volume_info.get("imageLinks", {}).get("thumbnail"),
                    "rating": volume_info.get("averageRating"),
                }
                books.append(book)

            return Response(books, status=status.HTTP_200_OK)

        except requests.exceptions.RequestException as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
