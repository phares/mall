from django import template

from oscar.core.compat import assignment_tag
from oscar.core.loading import get_model
register = template.Library()
Brand = get_model('catalogue', 'brand')
Product = get_model('catalogue', 'product')

assignment_tag = assignment_tag(register)


@assignment_tag(name="brand_list")
def get_list_of_brands():
    b = Brand.objects.all()
    return b
