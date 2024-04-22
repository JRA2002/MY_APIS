from .models import Product
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ProductSerializer

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer