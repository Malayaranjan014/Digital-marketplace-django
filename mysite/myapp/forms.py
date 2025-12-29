from django import forms 
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'file']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': (
                    'w-full px-3 py-2 text-sm '
                    'border border-gray-300 rounded-md '
                    
                ),
                'placeholder': 'Enter product name'
            }),
            'description': forms.Textarea(attrs={
                'class': (
                    'w-full px-3 py-2 text-sm '
                    'border border-gray-300 rounded-md '
                    
                ),
                'rows': 4,
                'placeholder': 'Enter product description'
            }),
            'price': forms.NumberInput(attrs={
                'class': (
                    'w-full px-3 py-2 text-sm '
                    'border border-gray-300 rounded-md '
                    
                ),
                'placeholder': 'Enter price'
            }),
            'file': forms.ClearableFileInput(attrs={
                'class': (
                    'w-full text-sm text-gray-700 '
                    'file:mr-4 file:py-2 file:px-4 '
                    'file:rounded-md file:border-0 '
                    'file:text-sm file:font-semibold '
                    
                )
            }),
        }

