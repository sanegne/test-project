from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

app_name = 'apiapp'

router = DefaultRouter()
router.register(r'books', BookViewSet, basename="books")

urlpatterns = [
    path('', include(router.urls)),
]
