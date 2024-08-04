from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView
from book import urls
from frontend import urls as frontend_urls

urlpatterns = [
    # AUTH
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('register/', RegisterView.as_view(), name='register'),

    path('frontend/', include(frontend_urls), name="frontend"),

    # recommendations related
    path('community/', include(urls),  name="community")
]