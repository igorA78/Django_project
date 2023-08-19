from datetime import datetime
from random import randint

from django.core.management import BaseCommand

from catalog.models import Product

class Command(BaseCommand):
    def handle(self, *args, **options):
        product_list = [{'product_name': 'Тыква', 'product_description': 'Желтая',
                         'product_category': 'Овощи',
                         'product_price': 60, 'create_date': datetime.now()},
                        {'product_name': 'Морковь', 'product_description': 'Сочная',
                         'product_category': 'Овощи',
                         'product_price': 70, 'create_date': datetime.now()},
                        {'product_name': 'Апельсин', 'product_description': 'Оранжевый',
                         'product_category': 'Фрукты',
                         'product_price': 80, 'create_date': datetime.now()},
                        {'product_name': 'Огурцы', 'product_description': 'Зеленые',
                         'product_category': 'Овощи',
                         'product_price': 90, 'create_date': datetime.now()},
                        ]
        products_for_create = []
        Product.objects.all().delete()
        for product in product_list:
            products_for_create.append(Product(**product))
        Product.objects.bulk_create(products_for_create)
