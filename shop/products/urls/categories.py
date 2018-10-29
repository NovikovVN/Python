from django.urls import include, path
from products.views import category_create, category_update, category_delete

app_name = 'categories'

urlpatterns = [
    path('create/', category_create, name='category_create'),
    path('update/<int:pk>/', category_update, name='category_update'),
    path('delete/<int:pk>/', category_delete, name='category_delete'),
]
