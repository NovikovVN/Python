from django.urls import include, path
from .views import products

urlpatterns = [
    path('', products),
    path('<int:pk>/', products)
]
