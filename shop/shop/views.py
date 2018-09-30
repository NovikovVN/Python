from django.shortcuts import render

def main(request):
    menu = (('', 'Главная'), ('/products', 'Каталог'), ('/contacts', 'Контакты'))
    return render(request, 'shop/index.html', context={'menu': menu, 'title': 'Главная'} )

def contacts(request):
    menu = (('/main', 'Главная'), ('/products', 'Каталог'), ('', 'Контакты'))
    return render(request, 'shop/contacts.html', context={'menu': menu, 'title': 'Контакты'} )
