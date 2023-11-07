from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<slug:choises_menu>/", views.menu, name="menu"),
    path("<slug:choises_menu>/<slug:menu_item>/", views.menu_item, name="menu_item"),
]