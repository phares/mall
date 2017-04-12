from django import template
from ..models import Carousel

register = template.Library()


@register.inclusion_tag("partials/carousel.html")
def load_carousel():
    carousel = Carousel.objects.all()
    length = carousel.count()
    return {
        "carousel_range": range(length),
        "carousel_length": length,
        "carousel_items": carousel
    }
