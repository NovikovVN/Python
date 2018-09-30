from django.urls import path

from .views import products, product_1, product_2, product_3

urlpatterns = [
    path('', products),
    path('1/', product_1),
    path('2/', product_2),
    path('3/', product_3)
]
