from django import forms

from products.models import Category, Product


class CategoryForm(forms.Form):
    title = forms.CharField(label='Название категории',
                            max_length=250,
                            required=True,
                            widget=forms.widgets.TextInput(attrs={'placeholder': 'Категория'}))

    snippet = forms.CharField(label='Краткое описание категории',
                              required=False,
                              widget=forms.widgets.Textarea(attrs={'placeholder': 'Введите описание категории'}))


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'snippet']
        widgets = {'title': forms.widgets.TextInput(attrs={'placeholder': 'Категория'}),
                   'snippet': forms.widgets.Textarea(attrs={'placeholder': 'Введите описание категории'})}


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'category', 'image', 'price', 'snippet', 'description']
        widgets = {'title': forms.widgets.TextInput(attrs={'placeholder': 'Товар'}),
                   'snippet': forms.widgets.Textarea(attrs={'placeholder': 'Введите описание товара'})}