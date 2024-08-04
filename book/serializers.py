# In your users/serializers.py file
from rest_framework import serializers
from .models import Book, Recommendation, Comment, Like
from user.serializers import CustomUserSerializer


class BookSerializer(serializers.ModelSerializer):
    """
    serializer for Book
    """

    class Meta:
        model = Book
        fields = ("id", "title", "author", "genre", "rating",)


class RecommendationSerializer(serializers.ModelSerializer):
    """
    serializer for recommendations
    """
    book = BookSerializer(read_only=True) 
    user = CustomUserSerializer(read_only=True)

    class Meta:
        model = Recommendation
        fields = ("book", "user", "created_at")


class CommentSerializer(serializers.ModelSerializer):
    """
    serializer for comments
    """        

    class Meta:
        model = Comment
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):
    """
    serializer for comments
    """        

    class Meta:
        model = Like
        fields = "__all__"


class GoogleBookSerializer(serializers.Serializer):
    """
    serializer for comments
    """        
    pass