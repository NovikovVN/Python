from json import load
from django.shortcuts import render

def get_menu():
    with open('data/menu_list.json', encoding='utf-8') as file:
        return load(file).items()

def main(request):
    title = 'Главная'
    return render(request, 'shop/index.html', context={'menu': get_menu(), 'title': title} )

def contacts(request):
    title = 'Контакты'
    return render(request, 'shop/contacts.html', context={'menu': get_menu(), 'title': title} )
