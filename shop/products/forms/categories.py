from django import forms

from products.models import Category


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'snippet']
        widgets = {'title': forms.widgets.TextInput(attrs={'placeholder': 'Категория'}),
                   'snippet': forms.widgets.Textarea(attrs={'placeholder': 'Введите описание категории'})}