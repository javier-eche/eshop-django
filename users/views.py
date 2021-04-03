from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from users.serializers import UserLoginSerializer, UserModelSerializer, UserSignUpSerializer

from users.models import User

class UserViewSet(viewsets.GenericViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserModelSerializer

    @action(detail=False, methods=['get'])
    def all(self, request):
        queryset = User.objects.all()
        serializer = UserModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserModelSerializer(user)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def signup(self, request):
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def logout(self, request):
        logout(request)
        data = {'success': 'Sucessfully logged out'}
        return Response(data, status=status.HTTP_200_OK)
        