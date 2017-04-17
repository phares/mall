from oscar.apps.catalogue.app import CatalogueApplication as BaseCatalogueApplication
from oscar.apps.catalogue.app import url
from .views import BrandsView

class CatalogueApplication(BaseCatalogueApplication):
    def get_urls(self):
        urlpatterns = super(CatalogueApplication, self).get_urls()
        urlpatterns += [
            url(r'^brand/(?P<brand>[\w-]+)/$', BrandsView.as_view(), name='brand')
            ]
        return self.post_process_urls(urlpatterns)

application = CatalogueApplication()
