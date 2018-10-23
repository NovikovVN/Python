from django.db import models

class Contact(models.Model):
    author = models.CharField(verbose_name='ФИО',
                             max_length=250)

    topic = models.CharField(verbose_name='Тема',
                             max_length=250)

    message = models.TextField(verbose_name='Сообщение',
                               blank=True)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.created