from django.core.paginator import Paginator
from django.shortcuts import (render, redirect, get_list_or_404, get_object_or_404)
from django.urls import reverse_lazy

from django.views.generic import (ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)

from products.forms import ProductModelForm
from products.models import Product

from shop.views import get_menu
from random import shuffle


class ProductListView(ListView):
    model = Product
    template_name = 'products/catalog.html'
    context_object_name = 'product_items'
    paginate_by = 4


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product.html'
    context_object_name = 'obj'


class ProductCreateView(CreateView):
    model = Product
    template_name = 'products/create.html'
    form_class = ProductModelForm
    success_url = reverse_lazy('products:catalog')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'products/create.html'
    form_class = ProductModelForm
    success_url = reverse_lazy('products:catalog')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/delete.html'
    success_url = reverse_lazy('products:catalog')


def product_create(request):
    title = 'Добавить товар'
    template_name = 'products/create.html'
    success_url = reverse_lazy('products:catalog')
    form = ProductModelForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect(success_url)

    context={'form': form,
             'title': title,
             'menu': get_menu()}

    return render(request, template_name, context)


def product_update(request, pk):
    title = 'Редактировать товар'
    template_name = 'products/create.html'
    success_url = reverse_lazy('products:catalog')
    obj = get_object_or_404(Product, pk=pk)

    form = ProductModelForm(instance=obj)

    if request.method == 'POST':
        form = ProductModelForm(request.POST,
                                instance=obj)
        if form.is_valid():
            form.save()

            return redirect(success_url)

    context={'form': form,
             'title': title,
             'menu': get_menu()}

    return render(request, template_name, context)


def product_delete(request, pk):
    title = 'Удалить товар'
    template_name = 'products/delete.html'
    success_url = reverse_lazy('products:catalog')
    obj = get_object_or_404(Product, pk=pk)

    form = ProductModelForm(instance=obj)

    if request.method == 'POST':
        form = ProductModelForm(request.POST,
                                instance=obj)
        if form.is_valid():
            obj.delete()

            return redirect(success_url)

    context={'form': form,
             'title': title,
             'menu': get_menu()}

    return render(request, template_name, context)


def catalog(request):
    title = 'Каталог'
    template_name = 'products/catalog.html'
    product_query = get_list_or_404(Product)
    shuffle(product_query)

    paginator = Paginator(product_query, 4)
    page = request.GET.get('page')
    product_items = paginator.get_page(page)

    context={'product_items': product_items,
             'title': title,
             'menu': get_menu()}

    return render(request, template_name, context)


def product(request, pk):
    obj = get_object_or_404(Product, pk=pk)

    template_name = 'products/product.html'
    context={'obj': obj,
             'menu': get_menu()}

    return render(request, template_name, context)