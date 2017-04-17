from django.conf.urls import url
from oscar.apps.dashboard.catalogue.app import CatalogueApplication as BaseCatalogueApplication
from .views import *

class CatalogueApplication(BaseCatalogueApplication):
    def get_urls(self):
        urlpatterns = super(CatalogueApplication, self).get_urls()
        urlpatterns += [
            url(r'^brands/$', BrandListView.as_view(), name='catalogue-brand-list'),
            url(r'^brands/new/$', BrandCreateView.as_view(), name='catalogue-brand-create'),
            url(r'^brands/(?P<pk>[0-9]+)/update/$', BrandUpdateView.as_view(), name='catalogue-brand-edit'),
            url(r'^brands/(?P<pk>[0-9]+)/delete/$', BrandDeleteView.as_view(), name='catalogue-brand-delete'),
            ]
        return self.post_process_urls(urlpatterns)

application = CatalogueApplication()
