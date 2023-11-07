from django.db import models


class Menu(models.Model):

    name = models.CharField(max_length=200)
    url = models.CharField(max_length=100, blank=False, null=False, unique=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'
    

class MenuItems(models.Model):

    name = models.CharField(max_length=200)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, blank=False, null=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='children', blank=True, null=True, default=0)
    url = models.CharField(max_length=100, blank=False, null=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Menu item'
        verbose_name_plural = 'Menu items'