from django.urls import path
from .views import ProductCreateApi, ProductListApi, ProductUpdateApi, ProductDeleteApi

urlpatterns = [
    path('', ProductListApi.as_view()),
    path('create', ProductCreateApi.as_view()),
    path('<int:pk>', ProductUpdateApi.as_view()),
    path('<int:pk>/delete', ProductDeleteApi.as_view()),
]