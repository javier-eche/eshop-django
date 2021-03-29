from django.shortcuts import render
from .models import Order
from .serializers import OrderSerializer

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class OrderCreateApi(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, )
    authentication_class = (TokenAuthentication,)

class OrderListApi(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDeleteApi(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer