from django.shortcuts import render

from .models import Category
from .serializers import CategorySerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class CategoryCreateApi(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated, )
    authentication_class = (TokenAuthentication,)

class CategoryListApi(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDeleteApi(generics.DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer