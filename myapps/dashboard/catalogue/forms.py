from django import forms

from oscar.apps.dashboard.catalogue.forms import ProductForm as ProductF
from oscar.core.loading import get_model
Product = get_model('catalogue', 'Product')
Brand = get_model('catalogue', 'Brand')

class ProductForm(ProductF):
    class Meta:
        model = Product
        fields = [
            'title', 'upc', 'description', 'brand', 'is_discountable', 'on_sale', 'is_featured', 'structure']
        widgets = {
            'structure': forms.HiddenInput()
        }
class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ('name', 'slug')
