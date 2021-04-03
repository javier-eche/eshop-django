from django.shortcuts import render

from .models import Subcategory
from .serializers import SubcategorySerializer, SubcategorySerializerSave
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class SubcategoryCreateApi(generics.CreateAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializerSave
    permission_classes = (IsAuthenticated, )
    authentication_class = (TokenAuthentication, )


class SubcategoryListApi(generics.ListAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer

class SubcategoryUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializerSave 

class SubcategoryDeleteApi(generics.DestroyAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubcategorySerializer
