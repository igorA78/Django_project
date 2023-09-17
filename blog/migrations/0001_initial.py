# Generated by Django 4.2.4 on 2023-09-17 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True, verbose_name='заголовок')),
                ('slug', models.CharField(max_length=150, verbose_name='slug')),
                ('message', models.TextField(blank='True', null='True', verbose_name='содержимое')),
                ('preview', models.ImageField(blank='True', null='True', upload_to='blog/', verbose_name='превью')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='опубликовано (да/нет)')),
                ('views_count', models.IntegerField(default=0, verbose_name='количество просмотров')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
    ]
