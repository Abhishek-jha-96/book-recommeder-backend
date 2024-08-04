from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Book, Recommendation, Comment, Like


class BookAdmin(ModelAdmin):
    list_display = (
        "id",
        "title",
        "author",
        "genre",
        "publication_date",
        "published_by",
    )
    list_filter = ("genre", "publication_date")
    search_fields = ("title", "author")


class RecommedationAdmin(ModelAdmin):
    list_display = (
        "id",
        "book",
        "user",
        "created_at",
    )
    list_filter = ("created_at",)
    search_fields = ("book", "user")


class CommentAdmin(ModelAdmin):
    list_display = (
        "id",
        "recommendation",
        "user",
        "created_at",
    )
    list_filter = ("recommendation", "created_at")
    search_fields = ("recommendation", "user")


class LikeAdmin(ModelAdmin):
    list_display = (
        "id",
        "recommendation",
        "user",
        "created_at",
    )
    list_filter = ("recommendation", "created_at")
    search_fields = ("recommendation", "user")


admin.site.register(Book, BookAdmin)
admin.site.register(Recommendation, RecommedationAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)
