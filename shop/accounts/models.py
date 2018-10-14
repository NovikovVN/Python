from django.db import models

from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    avatar = models.ForeignKey('images.Image',
                               on_delete=models.PROTECT,
                               verbose_name='Аватар',
                               blank=True,
                               null=True)

    phone = models.CharField(verbose_name='Телефон',
                             max_length=12,
                             blank=True,
                             null=True)

    def __str__(self):
        return self.username