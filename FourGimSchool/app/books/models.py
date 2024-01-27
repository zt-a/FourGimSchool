from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Book(models.Model):
    book_name = models.CharField(max_length=255, verbose_name='Название книги')
    pdf_book = models.FileField(upload_to='books/', verbose_name='Книга (PDF)')
    book_image = models.ImageField(upload_to='books_image/', verbose_name='Изображение книги')
    slug = models.SlugField(unique=True, db_index=True, verbose_name='URL')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создание')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.book_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.book_name

    def get_absolute_url(self):
        return reverse('books:detail_book', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
