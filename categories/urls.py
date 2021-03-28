from django.urls import path
from .views import CategoryCreateApi, CategoryListApi, CategoryUpdateApi, CategoryDeleteApi

urlpatterns = [
    path('', CategoryListApi.as_view()),
    path('create', CategoryCreateApi.as_view()),
    path('<int:pk>', CategoryUpdateApi.as_view()),
    path('<int:pk>/delete', CategoryDeleteApi.as_view()),  
]