from random import shuffle

from django.shortcuts import (render, redirect, get_list_or_404, get_object_or_404)
from django.urls import reverse_lazy

from products.forms import CategoryModelForm, ProductModelForm
from products.models import Category, Product

from shop.views import get_menu

##def category_create(request):
##    template_name = 'products/create.html'
##    success_url = reverse_lazy('products:catalog')
##    form = CategoryForm(request.POST)
##    context={'form': form, 'menu': get_menu()}
##
##    if request.method == 'POST':
##        if form.is_valid():
##            title = form.cleaned_data.get('title')
##            snippet = form.cleaned_data.get('snippet')
##
##            Category.objects.create(title=title,
##                                    snippet=snippet)
##
##            return redirect(success_url)
##
##    return render(request, template_name, context)

#def category_model_create(request):
def category_create(request):
    title = 'Добавить категорию'
    template_name = 'products/create.html'
    success_url = reverse_lazy('products:catalog')
    form = CategoryModelForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect(success_url)

    context={'form': form,
             'title': title,
             'menu': get_menu()}

    return render(request, template_name, context)


def category_update(request, pk):
    title = 'Редактировать категорию'
    template_name = 'products/create.html'
    success_url = reverse_lazy('products:catalog')
    obj = get_object_or_404(Category, pk=pk)

    form = CategoryModelForm(instance=obj)

    if request.method == 'POST':
        form = CategoryModelForm(request.POST,
                                 instance=obj)
        if form.is_valid():
            form.save()

            return redirect(success_url)

    context={'form': form,
             'title': title,
             'menu': get_menu()}

    return render(request, template_name, context)


def category_delete(request, pk):
    title = 'Удалить категорию'
    template_name = 'products/delete.html'
    success_url = reverse_lazy('products:catalog')
    obj = get_object_or_404(Category, pk=pk)

    form = CategoryModelForm(instance=obj)

    if request.method == 'POST':
        form = CategoryModelForm(request.POST,
                                 instance=obj)
        if form.is_valid():
            obj.delete()

            return redirect(success_url)

    context={'form': form,
             'title': title,
             'menu': get_menu()}

    return render(request, template_name, context)


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
    product_items = get_list_or_404(Product)
    shuffle(product_items)
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