from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class ContactModel(models.Model):
    subject = models.CharField(max_length=255, verbose_name="Тема")
    name = models.CharField(max_length=100, verbose_name="Имя", null=True, blank=True)
    email = models.EmailField(verbose_name="E-mail", null=True, blank=True)
    message = models.TextField(verbose_name="Сообщение")
    time_create = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Время обновление', auto_now=True)
    is_published = models.BooleanField(verbose_name='Публикация', default=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратные связи'
        ordering = ['-time_create', 'id']


class FeedbackModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    surname = models.CharField(max_length=100, verbose_name="Фамилия", null=True, blank=True)
    email = models.EmailField(verbose_name="E-mail", null=True, blank=True)
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона', null=True, blank=True)
    message = models.TextField(verbose_name="Введите отзыв")
    time_create = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Время обновление', auto_now=True)
    is_published = models.BooleanField(verbose_name='Публикация', default=True)

    def __str__(self):
        return f'{self.name} {self.surname}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-time_create', 'id']


class RulesModel(models.Model):
    number_rule = models.IntegerField(verbose_name='Номер правило', unique=True)
    title = models.CharField(max_length=255, verbose_name='Название правило')
    slug = models.SlugField(verbose_name='URL', unique=True)
    description = models.TextField(verbose_name='Описание правило')

    time_create = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Время обновление', auto_now=True)
    is_published = models.BooleanField(verbose_name='Публикация', default=True)

    def __str__(self):
        return f'{self.number_rule}: {self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.number_rule} {self.title}")
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('main:detail_rules', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Правило'
        verbose_name_plural = 'Правилы'
        ordering = ['number_rule', 'id', 'time_create']


class CategoryModel(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)
    slug = models.SlugField(verbose_name='URL', unique=True)

    time_create = models.DateTimeField(verbose_name='Время создание', auto_now_add=True)
    time_update = models.DateTimeField(verbose_name='Время обновление', auto_now=True)
    is_published = models.BooleanField(verbose_name='Публикация', default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('categories', kwargs={'slug': self.slug})

