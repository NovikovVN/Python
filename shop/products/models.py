from django.db import models

class Category(models.Model):
    title = models.CharField(verbose_name='Название категории',
                             max_length=250,
                             unique=True)

    snippet = models.TextField(verbose_name='Краткое описание категории',
                               null=True,
                               blank=True)


    modified = models.DateTimeField(auto_now=True)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(verbose_name='Название товара',
                             max_length=250,
                             unique=True)

    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 verbose_name='Категория товара')

    image = models.ForeignKey('images.Image',
                              on_delete=models.PROTECT,
                              verbose_name='Изображение товара')

    price = models.DecimalField(verbose_name='Стоимость товара',
                                max_digits=12,
                                decimal_places=2,
                                default=0)

    snippet = models.TextField(verbose_name='Краткое описание товара',
                               null=True,
                               blank=True)

    description = models.TextField(verbose_name='Полное описание товара',
                                   null=True,
                                   blank=True)

    modified = models.DateTimeField(auto_now=True)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Cup(Product):
    pass


class Scarf(Product):
    pass


class Tshirt(Product):
    pass