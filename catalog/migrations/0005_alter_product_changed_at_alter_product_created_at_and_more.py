# Generated by Django 4.2.4 on 2023-09-19 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_product_changed_at_alter_product_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='changed_at',
            field=models.DateField(auto_now=True, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='userquestion',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Дата'),
        ),
    ]
