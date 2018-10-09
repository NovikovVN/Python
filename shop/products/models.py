from django.db import models


class Product(models.Model):
    name = models.CharField(verbose_name='Обозначение товара',
                            max_length=64,
                            unique=True)

    image = models.ImageField(verbose_name='Изображение товара',
                              upload_to='media/')

    snippet = models.CharField(verbose_name='Краткое описание товара',
                               max_length=128,
                               null=True,
                               blank=True)

    description = models.TextField(verbose_name='Полное описание товара',
                                   null=True,
                                   blank=True)

    def __str__(self):
        return self.name


class Cup(Product):
    pass


class Scarf(Product):
    pass


class Tshirt(Product):
    pass