# Generated by Django 4.2.4 on 2023-08-19 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Создано в'),
        ),
    ]
