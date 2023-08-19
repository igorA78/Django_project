from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Наименование')
    product_description = models.TextField(verbose_name='Описание')
    product_image = models.ImageField(upload_to='products/', verbose_name='Изображение', **NULLABLE)
    product_category = models.CharField(max_length=50, verbose_name='Категория')
    product_price = models.IntegerField(verbose_name='Цена')
    create_date = models.DateField(verbose_name='Дата создания')
    change_date = models.DateField(verbose_name='Дата изменения', **NULLABLE)

    def __str__(self):
        return (f'{self.product_name} {self.product_description} {self.product_image} {self.product_category} '
                f'{self.product_price} {self.create_date} {self.change_date}')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Наименование')
    category_description = models.TextField(verbose_name='Описание')
   # created_at = models.CharField(max_length=20, verbose_name='Создано в', **NULLABLE)

    def __str__(self):
        return f'{self.category_name} {self.category_description}'
        #{self.created_at}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
