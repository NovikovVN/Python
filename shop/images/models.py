from django.db import models

class Image(models.Model):
    name = models.CharField(verbose_name='Название изображения',
                            max_length=250,
                            unique=True)

    value = models.ImageField(verbose_name='Изображение',
                              upload_to='images/')

    def __str__(self):
        return self.name