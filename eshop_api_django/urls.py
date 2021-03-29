
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('users.urls', 'users'), namespace='users')),
    path('api/v1/subcategories/', include('subcategories.urls')),
    path('api/v1/categories/', include('categories.urls')),
    path('api/v1/products/', include('products.urls')),
    path('api/v1/items/', include('item_order.urls')),
    path('api/v1/orders/', include('order.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
