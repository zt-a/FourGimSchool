from django.db import models


# Create your models here.
class Document(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    pdf_file = models.FileField(upload_to='documents/', verbose_name='Документ (PDF)')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создание')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
