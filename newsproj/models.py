from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse
from django.utils import timezone
from newsproj.models import *


class New(models.Model):
    author_new = models.ForeignKey('Author', on_delete=models.CASCADE, verbose_name='Автор')
    category_new = models.ManyToManyField('Category', verbose_name = 'Категория')
    date_create = models.DateTimeField(default=timezone.now, verbose_name = 'Дата публикации')
    description = models.TextField(verbose_name = 'Текст')
    name = models.CharField(max_length=50, unique=True, verbose_name = 'Заголовок')

    def __str__(self):
        return f'{self.name}: {self.date_create}: {self.category_new}: {self.description}: {self.author_new}'

    def get_absolute_url(self):
        return f'/news/'

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name.title()


class NewCategory(models.Model):
    new = models.ForeignKey(New, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Author(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return f'{self.name}'
