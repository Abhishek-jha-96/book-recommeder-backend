from rest_framework import generics
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema

from .models import CustomUser
from .serializers import CustomUserSerializer

@extend_schema(
    tags=["Register"],
)
class RegisterView(generics.CreateAPIView):
    """
    View for User Creation only.
    """

    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = CustomUserSerializer
