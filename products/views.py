from rest_framework import mixins, status, viewsets
from rest_framework.response import Response

from products.serializers import ProductModelSerializer, ProductSerializer

class ProductViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = ProductModelSerializer

    def create(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data, context={"request": self.request})
        serializer.is_valid(raise_exception=True)
        prod = serializer.save()
        data = ProductModelSerializer(prod).data
        return Response(data, status=status.HTTP_201_CREATED)