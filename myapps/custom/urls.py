from django.conf.urls import url, include

from .views import *

urlpatterns = [
    url(r'^dashboard/carousel/$', CarouselItemListView.as_view(), name='carousel-item-list'),
    url(r'^dashboard/carousel/new/$', CarouselItemCreateView.as_view(), name='carousel-item-create'),
    url(r'^dashboard/carousel/(?P<pk>[0-9]+)/update/$', CarouselItemUpdateView.as_view(), name='carousel-item-edit'),
    url(r'^dashboard/carousel/(?P<pk>[0-9]+)/delete/$', CarouselItemDeleteView.as_view(), name='carousel-item-delete'),
    url(r'^contact/$', ContactView.as_view(), name="contact"),
]
