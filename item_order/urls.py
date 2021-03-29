from django.urls import path
from .views import ItemCreateApi, ItemListApi

urlpatterns = [
    path('', ItemListApi.as_view()),
    path('create', ItemCreateApi.as_view()),
]