from django.shortcuts import (render, redirect, get_list_or_404, get_object_or_404)
from django.urls import reverse_lazy

from products.forms import CategoryModelForm
from products.models import Category

from shop.views import get_menu

def category_create(request):
    title = 'Добавить категорию'
    template_name = 'products/create.html'
    success_url = reverse_lazy('categories:catalog')
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
    success_url = reverse_lazy('categories:catalog')
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
    success_url = reverse_lazy('categories:catalog')
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