from django.utils.translation import ugettext_lazy as _
from django.core.paginator import EmptyPage, InvalidPage
from oscar.apps.catalogue.views import CatalogueView

class BrandsView(CatalogueView):
    """
    Browse all products by a brand in the catalogue
    """

    def get(self, request, *args, **kwargs):
        try:
            self.search_handler = self.get_search_handler(
                self.request.GET, request.get_full_path(), [], brand=kwargs["brand"])
        except InvalidPage:
            # Redirect to page one.
            messages.error(request, _('The given page number was invalid.'))
            return redirect('catalogue:index')
        return super(CatalogueView, self).get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        ctx = {}
        ctx['summary'] = _("All products of a brand")
        search_context = self.search_handler.get_search_context_data(
            self.context_object_name)
        ctx.update(search_context)
        return ctx
