from django.urls import path
from .views import (
    BookViewsets, 
    RecommendationViewsets, 
    CommentViewsets, 
    LikeViewsets, 
    GoogleBookView, 
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'book', BookViewsets, basename='book')
router.register(r'recommendations', RecommendationViewsets, basename='recommendations')
router.register(r'comment', CommentViewsets, basename='comments')
router.register(r'like', LikeViewsets, basename='likes')

urlpatterns = [
    path('google_library/', GoogleBookView.as_view(), name='googleLibrary'),
] + router.urls
