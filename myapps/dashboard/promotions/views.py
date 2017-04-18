from django.contrib import messages
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django_tables2 import SingleTableMixin, SingleTableView
from oscar.core.loading import get_class, get_model

from .forms import CarouselItemForm
from .tables import CarouselItemTable

CarouselItem = get_model("promotions", "CarouselItem")

class CarouselItemListView(SingleTableView):
    template_name = "dashboard/catalogue/carousel_list.html"
    table_class = CarouselItemTable
    context_table_name = 'carousel'

    def get_queryset(self):
        print(CarouselItem.objects.all())
        return CarouselItem.objects.all()

class CarouselItemMixin:
    def get_success_url(self):
        return reverse("dashboard:carousel-item-list")

class CarouselItemCreateView(CarouselItemMixin, CreateView):
    template_name = 'dashboard/catalogue/carousel_form.html'
    model = CarouselItem
    form_class = CarouselItemForm

    def get_context_data(self, **kwargs):
        ctx = super(CarouselItemCreateView, self).get_context_data(**kwargs)
        ctx['title'] = _("Add a new carousel item")
        return ctx

    def get_success_url(self):
        messages.info(self.request, _("Carousel item created successfully"))
        return super(CarouselItemCreateView, self).get_success_url()

class CarouselItemUpdateView(CarouselItemMixin, UpdateView):
    template_name = 'dashboard/catalogue/carousel_form.html'
    model = CarouselItem
    form_class = CarouselItemForm

    def get_context_data(self, **kwargs):
        ctx = super(CarouselItemUpdateView, self).get_context_data(**kwargs)
        ctx['title'] = _("Update a carousel item")
        return ctx

    def get_success_url(self):
        messages.info(self.request, _("CarouselItem updated successfully"))
        return super(CarouselItemUpdateView, self).get_success_url()

class CarouselItemDeleteView(CarouselItemMixin, DeleteView):
    template_name = 'dashboard/catalogue/carousel_delete.html'
    model = CarouselItem

    def get_success_url(self):
        messages.info(self.request, _("Carousel item deleted successfully"))
        return super(CarouselItemDeleteView, self).get_success_url()
