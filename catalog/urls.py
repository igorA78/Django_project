from django.urls import path
from django.views.decorators.cache import never_cache

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, UserQuestionCreateView, \
    ProductUpdateView, DeliveryCreateView, DeliveryUpdateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('contact/', UserQuestionCreateView.as_view(), name='contact'),
    path('view/<int:pk>', ProductDetailView.as_view(), name='view'),
    path('create/', never_cache(ProductCreateView.as_view()), name='create'),
    path('update/<int:pk>', never_cache(ProductUpdateView.as_view()), name='update'),
    path('create_delivery/<int:product_pk>', DeliveryCreateView.as_view(), name='create_delivery'),
    path('update_delivery/<int:pk>', DeliveryUpdateView.as_view(), name='update_delivery'),
]
