from django.conf.urls import url
from oscar.apps.dashboard.promotions.app import PromotionsDashboardApplication
from .views import *

class CatalogueApplication(PromotionsDashboardApplication):
    def get_urls(self):
        urlpatterns = super(CatalogueApplication, self).get_urls()
        urlpatterns += [
            url(r'^carousel/$', CarouselItemListView.as_view(), name='carousel-item-list'),
            url(r'^carousel/new/$', CarouselItemCreateView.as_view(), name='carousel-item-create'),
            url(r'^carousel/(?P<pk>[0-9]+)/update/$', CarouselItemUpdateView.as_view(), name='carousel-item-edit'),
            url(r'^carousel/(?P<pk>[0-9]+)/delete/$', CarouselItemDeleteView.as_view(), name='carousel-item-delete'),
            ]
        return self.post_process_urls(urlpatterns)

application = CatalogueApplication()
