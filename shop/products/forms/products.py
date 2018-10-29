from django import forms

from products.models import Product


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'category', 'image', 'price', 'snippet', 'description']
        widgets = {'title': forms.widgets.TextInput(attrs={'placeholder': 'Товар'}),
                   'snippet': forms.widgets.Textarea(attrs={'placeholder': 'Введите описание товара'})}