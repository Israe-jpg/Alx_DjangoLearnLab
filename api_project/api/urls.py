# api/urls.py
from django.urls import path, include
from .views import BookViewSet
from .views import BookList


from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
     path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # Token authentication endpoint
]


# Create a router and register our viewset with it
router = DefaultRouter()
router.register(r'books', BookViewSet)



