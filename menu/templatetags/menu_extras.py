from django import template
from django.template import RequestContext

from menu.models import MenuItems


register = template.Library()


def create_menu_recursive(item, current_path):
    children = item.children.all()
    ch = list()
    active = True if item.url == current_path else False
    if children:
        for i in children:
            menu, ch_active = create_menu_recursive(i, current_path)
            if not active:
                active = ch_active 
            ch.append(menu)
    return    {
                'id': item.pk,
                'url': item.url,
                'name': item.name,
                'active': active,
                'parent': item.parent,
                'children': ch
            }, active


@register.inclusion_tag("menu/result.html", takes_context=True)
def draw_menu(context: RequestContext, name: str = ''):
    current_path = context.request.path.split('/')[-2]
    data = MenuItems.objects.select_related().filter(menu__name=name, parent__isnull=True)  
    menu = []
    for item in data:
        menu.append(create_menu_recursive(item, current_path)[0])  
    return {'menu_items':  menu, 'choises_menu': name}