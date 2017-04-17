from oscar.apps.promotions.views import HomeView as Home

from oscar.core.loading import get_class, get_model

Product = get_model('catalogue', 'product')

class HomeView(Home):
    def get_context_data(self, **kwargs):
        context = {}
        context["featured_products"] =  Product.browsable.base_queryset().filter(is_featured=True)[:24]

        return context
