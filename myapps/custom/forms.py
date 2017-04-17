from django import forms
from .models import CarouselItem

from oscar.core.loading import  get_model

Product = get_model("catalogue", "Product")

class CarouselItemForm(forms.ModelForm):
    link = forms.URLField(required=False)
    product = forms.ModelChoiceField(queryset=Product.objects.all(), required=False)
    class Meta:
        model = CarouselItem
        fields = ('title', 'description', 'image', 'link', "product")
