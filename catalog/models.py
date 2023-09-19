from datetime import date

from django.db import models

NULLABLE = {'null': 'True', 'blank': 'True'}


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    image = models.ImageField(upload_to='products/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='id категории')
    price = models.IntegerField(verbose_name='Цена', **NULLABLE)
    created_at = models.DateField(verbose_name='Дата создания', auto_now_add=True)
    changed_at = models.DateField(verbose_name='Дата изменения', auto_now=True)

    def __str__(self):
        return f'{self.name}'

    @property
    def current_delivery(self):
        return self.delivery_set.filter(is_current=True).last()

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['category', 'name']


class CompanyContact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    icon_bootstrap = models.CharField(max_length=100, verbose_name='Иконка Bootstrap')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class UserQuestion(models.Model):
    user_name = models.CharField(max_length=150, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Почта')
    question = models.TextField(verbose_name='Вопрос')
    created_at = models.DateField(verbose_name='Дата', auto_now_add=True)

    def __str__(self):
        return f'{self.user_name}: {self.question[:20]}'

    class Meta:
        verbose_name = 'Вопрос пользователя'
        verbose_name_plural = 'Вопросы пользователей'



class Delivery(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Продукт')
    delivery_number = models.IntegerField(verbose_name='Номер')
    delivery_date = models.DateField(verbose_name='Дата доставки продукции')
    is_current = models.BooleanField(default=False, verbose_name='Текущая доставка (да/нет)')

    def __str__(self):
        return f'({self.delivery_number}) {self.delivery_date} - {self.product}'

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставки'

