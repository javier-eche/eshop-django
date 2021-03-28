from django.urls import path
from .views import SubcategoryCreateApi, SubcategoryListApi, SubcategoryUpdateApi, SubcategoryDeleteApi

urlpatterns = [
    path('', SubcategoryListApi.as_view()),
    path('create', SubcategoryCreateApi.as_view()),
    path('<int:pk>', SubcategoryUpdateApi.as_view()),
    path('<int:pk>/delete', SubcategoryDeleteApi.as_view()),
]