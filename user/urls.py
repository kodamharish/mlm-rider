from django.urls import path
from .views import *

urlpatterns = [
    path('riders/', RiderListCreateAPIView.as_view(), name='rider-list-create'),
    path('riders/<int:pk>/', RiderDetailAPIView.as_view(), name='rider-detail'),
]