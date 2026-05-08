from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category', 'is_published']
        widgets = {
            'is_published': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'id': 'is_published'
            }),
            'description': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'is_published': 'Опубликовать товар на сайте',
        }