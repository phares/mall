from django.conf import settings
from django.views.generic.list import MultipleObjectMixin

from oscar.core.loading import get_model
Product = get_model('catalogue', 'Product')


class SimpleProductSearchHandler(MultipleObjectMixin):
    """
    A basic implementation of the full-featured SearchHandler that has no
    faceting support, but doesn't require a Haystack backend. It only
    supports category browsing.
    Note that is meant as a replacement search handler and not as a view
    mixin; the mixin just does most of what we need it to do.
    """
    paginate_by = settings.OSCAR_PRODUCTS_PER_PAGE

    def __init__(self, request_data, full_path, categories=None, brand=None):
        self.categories = categories
        self.brand = brand
        self.kwargs = {'page': request_data.get('page', 1)}
        self.set_range(request_data)
        self.object_list = self.get_queryset()

    def set_range(self, request_data):
        max_price, min_price = request_data.get("max"), request_data.get("min")
        self.min = int(min_price) if min_price and min_price.isdecimal() else None
        self.max = int(max_price) if max_price and max_price.isdecimal() else None

    def get_queryset(self):
        qs = Product.browsable.base_queryset()
        if self.min:
            qs = qs.filter(price__gte=self.min)
        if self.max:
            qs = qs.filter(price__lte=self.max)
        if self.categories:
            qs = qs.filter(categories__in=self.categories).distinct()
        if self.brand:
            qs = qs.filter(brand__slug=self.brand)
        return qs

    def get_search_context_data(self, context_object_name):
        # Set the context_object_name instance property as it's needed
        # internally by MultipleObjectMixin
        self.context_object_name = context_object_name
        context = self.get_context_data(object_list=self.object_list)
        context[context_object_name] = context['page_obj'].object_list
        return context
