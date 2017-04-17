from django.contrib import messages
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from django_tables2 import SingleTableMixin, SingleTableView
from oscar.core.loading import get_class, get_model

from  .forms import BrandForm
from .tables import BrandTable

Brand = get_model('catalogue', 'Brand')

# Create your views here.
class BrandListView(SingleTableView):
    template_name = "dashboard/catalogue/brand_list.html"
    table_class = BrandTable
    context_table_name = 'brands'

    def get_queryset(self):
        return Brand.objects.all()


    # def get_context_data(self, *args, **kwargs):
    #     ctx = super(CategoryListView, self).get_context_data(*args, **kwargs)
    #     ctx['child_categories'] = Category.get_root_nodes()
    #     return ctx
class BrandMixin:
    def get_success_url(self):
        return reverse("dashboard:catalogue-brand-list")

class BrandCreateView(BrandMixin, CreateView):
    template_name = 'dashboard/catalogue/brand_form.html'
    model = Brand
    form_class = BrandForm

    def get_context_data(self, **kwargs):
        ctx = super(BrandCreateView, self).get_context_data(**kwargs)
        ctx['title'] = _("Add a new brand")
        return ctx

    def get_success_url(self):
        messages.info(self.request, _("Brand created successfully"))
        return super(BrandCreateView, self).get_success_url()

class BrandUpdateView(BrandMixin, UpdateView):
    template_name = 'dashboard/catalogue/brand_form.html'
    model = Brand
    form_class = BrandForm

    def get_context_data(self, **kwargs):
        ctx = super(BrandUpdateView, self).get_context_data(**kwargs)
        ctx['title'] = _("Update a brand")
        return ctx

    def get_success_url(self):
        messages.info(self.request, _("Brand updated successfully"))
        return super(BrandUpdateView, self).get_success_url()

class BrandDeleteView(BrandMixin, DeleteView):
    template_name = 'dashboard/catalogue/category_delete.html'
    model = Brand

    def get_success_url(self):
        messages.info(self.request, _("Brand deleted successfully"))
        return super(BrandDeleteView, self).get_success_url()
