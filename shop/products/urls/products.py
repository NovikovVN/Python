from django.urls import include, path
from products.views import (
##                          product_create, product_update, product_delete,
##                          catalog, product,
                            ProductListView, ProductDetailView,
                            ProductCreateView, ProductUpdateView, ProductDeleteView,
                            )

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='catalog'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product'),

    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
]

##urlpatterns = [
##    path('', catalog, name='catalog'),
##    path('<int:pk>/', ProductDetailView.as_view(), name='product'),
##
##    path('create/', product_create, name='product_create'),
##    path('update/<int:pk>', product_update, name='product_update'),
##    path('delete/<int:pk>', product_delete, name='product_delete'),
##]