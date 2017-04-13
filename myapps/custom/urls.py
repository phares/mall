from django.conf.urls import url, include

from .views import ContactView

urlpatterns = [
    url(r'^contact/$', ContactView.as_view()),
]
