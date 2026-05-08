from django import forms
from django.core.exceptions import ValidationError
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'is_published']
        widgets = {
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'is_published': 'Опубликовать товар на сайте',
        }


    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise ValidationError('Цена должна быть больше 0!')
        return price