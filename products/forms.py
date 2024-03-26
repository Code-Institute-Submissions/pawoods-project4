from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, SubCategory, Brand


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        sub_categories = SubCategory.objects.all()
        sub_friendly_names = [(c.id, c.get_friendly_name()) for c in sub_categories]

        brands = Brand.objects.all()
        brand_friendly_names = [(b.id, b.get_friendly_name()) for b in brands]

        self.fields['sub_category'].choices = sub_friendly_names
        self.fields['brand'].choices = brand_friendly_names

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'stripe-style-input'
