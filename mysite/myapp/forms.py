from django import forms 
from .models import Product
from django.contrib.auth.models import User 
from django.contrib.auth.forms import AuthenticationForm


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'file']
        # Adding some styling to the form fields
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



class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full border px-3 py-2 rounded-md focus:outline-none  focus:ring-2'
        })
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={
            'class': 'w-full border px-3 py-2 rounded-md focus:outline-none focus:ring-2 '
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full border px-3 py-2 rounded-md focus:outline-none focus:ring-2 '
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full border px-3 py-2 rounded-md focus:outline-none focus:ring-2 '
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'w-full border px-3 py-2 rounded-md focus:outline-none focus:ring-2 '
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full border px-3 py-2 rounded-md focus:outline-none focus:ring-2 '
            }),
        }
#check password 
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password') != cleaned_data.get('password2'):
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data


#hashes password 
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user





# create custom login form 
class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'w-full border px-3 py-2 rounded-md focus:outline-none focus:ring-2 '
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full border px-3 py-2 rounded-md focus:outline-none focus:ring-2 '
        })
    )
