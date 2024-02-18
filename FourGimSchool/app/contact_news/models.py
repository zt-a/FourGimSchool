from django.db import models


class Contact(models.Model):
    email = models.EmailField(verbose_name='E-mail')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создании')

    def __str__(self):
        return self.email
