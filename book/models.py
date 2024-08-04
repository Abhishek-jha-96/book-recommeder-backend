from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from user.models import CustomUser
from book import constants


class Book(models.Model):
    """
    Book model for entries recommended by users.
    """

    title = models.CharField(max_length=255, help_text=constants.TITLE_HELP_TEXT)
    author = models.CharField(max_length=255, help_text=constants.AUTHOR_HELP_TEXT)
    genre = models.CharField(max_length=100, help_text=constants.GENER_HELP_TEXT)
    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        help_text=constants.RATING_HELP_TEXT,
    )
    publication_date = models.DateTimeField(
        auto_now_add=True, help_text=constants.PUB_DATE_HELP_TEXT
    )
    published_by = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="created_by",
        help_text=constants.CREATED_HELP_TEXT,
    )

    class Meta:
        unique_together = ["title", "author"]
        indexes = [
            models.Index(fields=["title", "author"]),
        ]

    def __str__(self):
        return f"{self.title} by {self.author}"


class Recommendation(models.Model):
    """
    Recommendation model to track user interactions with book recommendations.
    """

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="recommendations",
        help_text=constants.BOOK_HELP_TEXT,
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="user_recommendations",
        help_text=constants.USER_HELP_TEXT,
    )
    created_at = models.DateTimeField(
        auto_now_add=True, help_text=constants.CREATED_HELP_TEXT
    )

    class Meta:
        unique_together = ("book", "user")

    def to_representation(self):
        rep = {
            "book": self.book,
            "user": self.user,
            "liked_by": [like.user for like in self.likes.all()],
            "comments": [comment for comment in self.comments.all()],
            "created_at": self.created_at,
        }
        return rep

    def __str__(self):
        return f"{self.book.title}"

class Comment(models.Model):
    """
    Comment model for comments on book recommendations.
    """

    recommendation = models.ForeignKey(
        Recommendation,
        on_delete=models.CASCADE,
        related_name="comments",
        help_text=constants.BOOK_CMNT_HELP_TEXT,
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="book_comments",
        help_text=constants.CMNT_USER_HELP_TEXT,
    )
    message = models.TextField(help_text=constants.MESSAGE_HELP_TEXT)
    created_at = models.DateTimeField(
        auto_now_add=True, help_text=constants.CMNT_CREATE_HELP_TEXT
    )


class Like(models.Model):
    """
    Like model to track which user liked which recommendation.
    """

    recommendation = models.ForeignKey(
        Recommendation,
        on_delete=models.CASCADE,
        related_name="likes",
        help_text=constants.BOOK_HELP_TEXT,
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="likes",
        help_text=constants.USER_HELP_TEXT,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("recommendation", "user")
