from django import template
from oscar.core.loading import  get_model

CarouselItem = get_model("promotions", "CarouselItem")
register = template.Library()


@register.inclusion_tag("partials/carousel.html")
def load_carousel():
    carousel = CarouselItem.objects.all()
    length = carousel.count()
    return {
        "carousel_range": range(length),
        "carousel_length": length,
        "carousel_items": carousel
    }
