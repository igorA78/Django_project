# Generated by Django 4.2.4 on 2023-09-17 15:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('icon_bootstrap', models.CharField(max_length=100, verbose_name='Иконка Bootstrap')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='date_changing',
        ),
        migrations.RemoveField(
            model_name='product',
            name='date_creation',
        ),
        migrations.AddField(
            model_name='product',
            name='changed_at',
            field=models.DateField(default=datetime.date(2023, 9, 17), verbose_name='Дата изменения'),
        ),
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateField(default=datetime.date(2023, 9, 17), verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='id категории'),
        ),
    ]
