from django.urls import include, path
from products.views import (product_create, product_update, product_delete,
                            category_create, category_update, category_delete,
                            catalog, product)

app_name = 'products'

urlpatterns = [
    path('', catalog, name='catalog'),
    path('<int:pk>/', product, name='product'),

    path('create/', product_create, name='product_create'),
    path('<int:pk>/update', product_update, name='product_update'),
    path('<int:pk>/delete', product_delete, name='product_delete'),

    path('category/create/', category_create, name='category_create'),
    path('category/<int:pk>/update/', category_update, name='category_update'),
    path('category/<int:pk>/delete/', category_delete, name='category_delete'),
]
