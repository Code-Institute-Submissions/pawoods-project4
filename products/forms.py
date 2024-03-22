from django import forms
from .models import Product, Category, SubCategory, Brand


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        sub_categories = SubCategory.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in sub_categories]

        self.fields['sub_category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'stripe-style-input'