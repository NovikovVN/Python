from json import load
from django.shortcuts import render

def get_menu():
    with open('data/menu_list.json', encoding='utf-8') as file:
        return load(file).items()

product_items = (
('/products/1/', '/static/img/scarf_white.png', 'Белый MetalBonobo Scarf', 295),
('/products/2/', '/static/img/cup_black.png', 'Черная MetalBonobo Cup', 88),
('/products/3/', '/static/img/tshirt_red.png', 'Красная MetalBonobo T-shirt', 381)
)

def products(request, pk=None):
    if not(pk):
        title = 'Каталог'
        return render(request, 'products/catalog.html',
                      context={'menu': get_menu(),
                               'title': title,
                               'product_items': product_items[:][:3]} )
    elif pk == 1:
        title = 'MetalBonobo Scarf'
        return render(request, 'products/metalbonobo_scarf.html',
                      context={'menu': get_menu(),
                               'title': title,
                               'image': product_items[0][1],
                               'descr': product_items[0][2],
                               'price': product_items[0][3]} )

    elif pk == 2:
        title = 'MetalBonobo Cup'
        return render(request, 'products/metalbonobo_cup.html',
                      context={'menu': get_menu(),
                               'title': title,
                               'image': product_items[1][1],
                               'descr': product_items[1][2],
                               'price': product_items[1][3]} )

    elif pk == 3:
        title = 'MetalBonobo T-shirt'
        return render(request, 'products/metalbonobo_tshirt.html',
                      context={'menu': get_menu(),
                               'title': title,
                               'image': product_items[2][1],
                               'descr': product_items[2][2],
                               'price': product_items[2][3]} )