from django.urls import path
from .views import AssetListCreateView, AssetRetrieveUpdateDestroyView

urlpatterns = [
    path('assets/', AssetListCreateView.as_view(), name='asset-list-create'),
    path('assets/<int:pk>/', AssetRetrieveUpdateDestroyView.as_view(), name='asset-retrieve-update-destroy'),
]
