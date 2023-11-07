from django.shortcuts import render
from menu.models import Menu


def index(request):
    menu = Menu.objects.all()
    context = {'menu': menu }
    return render(request, 'menu/index.html', context)

def menu(request, choises_menu):
    menu = Menu.objects.all()
    context = {'menu': menu, 'choises_menu': choises_menu}
    return render(request, 'menu/one_menu.html', context)

def menu_item(request, choises_menu, menu_item):
    menu = Menu.objects.all()
    context = {'menu': menu, 'menu_name': choises_menu, 'choises_menu': choises_menu}
    return render(request, 'menu/one_menu.html', context)