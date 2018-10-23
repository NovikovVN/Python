from django.contrib.auth import authenticate, login
from django.shortcuts import render
from shop.views import get_menu

def login_view(request):
    title = 'Вход'

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user and user.is_active:
            login(request, user)
        else:
            pass

    return render(request, 'accounts/login.html', context={'menu': get_menu(), 'title': title} )
