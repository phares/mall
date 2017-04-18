from django import forms

from oscar.core.loading import  get_model

Product = get_model("catalogue", "Product")
CarouselItem = get_model("promotions", "CarouselItem")

class CarouselItemForm(forms.ModelForm):
    link = forms.URLField(required=False)
    product = forms.ModelChoiceField(queryset=Product.objects.all(), required=False)
    class Meta:
        model = CarouselItem
        fields = ('title', 'description', 'image', 'link', "product")
