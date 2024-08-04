from django.urls import path
from .views import (
    book_list,
    login
)


urlpatterns = [
    path('home', login, name="login"),
    path('book_list/', book_list, name='book_list'),
]
