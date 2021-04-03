from django.shortcuts import render

from .models import Item
from .serializers import ItemSerializer, ItemSerializerSave
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class ItemCreateApi(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = (IsAuthenticated, )
    authentication_class = (TokenAuthentication,)

class ItemListApi(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
