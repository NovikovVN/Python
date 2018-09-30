from django.shortcuts import render

product_items = (
('/products/1/', '/static/img/scarf_white.png', 'Белый MetalBonobo Scarf', 295),
('/products/2/', '/static/img/cup_black.png', 'Черная MetalBonobo Cup', 88),
('/products/3/', '/static/img/tshirt_red.png', 'Красная MetalBonobo T-shirt', 381)
)

def products(request):
    menu = (('/main', 'Главная'), ('', 'Каталог'), ('/contacts', 'Контакты'))
    return render(request, 'products/catalog.html',
                  context={'menu': menu,
                           'product_items': product_items[:][:3]} )

def product_1(request):
    menu = (('/main', 'Главная'), ('/products', 'Каталог'), ('/contacts', 'Контакты'))
    return render(request, 'products/metalbonobo_scarf.html',
                  context={'menu': menu,
                           'image': product_items[0][1],
                           'descr': product_items[0][2],
                           'price': product_items[0][3]} )

def product_2(request):
    menu = (('/main', 'Главная'), ('/products', 'Каталог'), ('/contacts', 'Контакты'))
    return render(request, 'products/metalbonobo_cup.html',
                  context={'menu': menu,
                           'image': product_items[1][1],
                           'descr': product_items[1][2],
                           'price': product_items[1][3]} )

def product_3(request):
    menu = (('/main', 'Главная'), ('/products', 'Каталог'), ('/contacts', 'Контакты'))
    return render(request, 'products/metalbonobo_tshirt.html',
                  context={'menu': menu,
                           'image': product_items[2][1],
                           'descr': product_items[2][2],
                           'price': product_items[2][3]} )