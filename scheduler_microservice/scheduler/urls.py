from django.urls import path
from .views import JobViewSet

urlpatterns = [
    path('jobs/', JobViewSet.as_view({'get': 'list', 'post': 'create'}), name='job-list'),
    path('jobs/<int:pk>/', JobViewSet.as_view({'get': 'retrieve'}), name='job-detail'),
]