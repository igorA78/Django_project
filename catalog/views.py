from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from catalog.forms import ProductForm, UserQuestionForm, DeliveryForm
from catalog.models import Category, Product, CompanyContact, UserQuestion, Delivery
from catalog.services import get_category_set


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = []
        categories = Category.objects.all()
        for category in categories:
            data.append({
                'category': category,
                'products': Product.objects.filter(category=category.pk),
            })
        data = sorted(data, key=lambda item: item['category'].pk)
        context['categories'] = get_category_set()
        return context


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('catalog:view', kwargs={'pk': self.object.pk})


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse_lazy('catalog:view', args=[self.kwargs['pk']])


class UserQuestionCreateView(CreateView):
    model = UserQuestion
    form_class = UserQuestionForm
    # company_contacts = CompanyContact.objects.all()
    # company_contacts = sorted(company_contacts, key=lambda item: item.pk)
    # extra_context = {'cont': company_contacts}
    success_url = reverse_lazy('catalog:contact')

    def get_context_data(self, **kwargs):
        return super().get_context_data( **kwargs)


class DeliveryCreateView(CreateView):
    model = Delivery
    form_class = DeliveryForm

    def get_success_url(self):
        return reverse('catalog:view', args=[self.kwargs['product_pk']])

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial']['product'] = Product.objects.get(pk=self.kwargs['product_pk'])
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['product'] = Product.objects.get(pk=self.kwargs['product_pk'])
        return context


class DeliveryUpdateView(UpdateView):
    model = Delivery
    form_class = DeliveryForm

    def get_success_url(self):
        return reverse_lazy('catalog:view', args=[self.object.product.pk])
