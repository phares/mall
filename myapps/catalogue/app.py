from oscar.apps.catalogue.app import CatalogueApplication
from oscar.apps.catalogue.app import url
from .views import BrandsView

class BaseCatalogueApplication(CatalogueApplication):
    def get_urls(self):
        urlpatterns = super(BaseCatalogueApplication, self).get_urls()
        urlpatterns += [
            url(r'^brand/(?P<brand>[\w-]+)/$', BrandsView.as_view(), name='edit-brand')
            ]
        return self.post_process_urls(urlpatterns)

application = BaseCatalogueApplication()
