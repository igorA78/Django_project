# Generated by Django 4.2.4 on 2023-09-19 18:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_userquestion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='changed_at',
            field=models.DateField(default=datetime.date(2023, 9, 19), verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateField(default=datetime.date(2023, 9, 19), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='userquestion',
            name='created_at',
            field=models.DateField(default=datetime.date(2023, 9, 19), verbose_name='Дата'),
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_number', models.IntegerField(verbose_name='Номер')),
                ('delivery_date', models.DateField(verbose_name='Дата доставки продукции')),
                ('is_current', models.BooleanField(default=False, verbose_name='Текущая доставка (да/нет)')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Доставка',
                'verbose_name_plural': 'Доставки',
            },
        ),
    ]
