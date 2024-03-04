from rest_framework import generics
from .models import Asset
from .serializers import AssetSerializer

# Create your views here.
class AssetListCreateView(generics.ListCreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

class AssetRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
