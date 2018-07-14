from GlobalCartapp.models import *
from django import forms


class AddItem(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ['id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
            'availability': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter availablecount'}),
            'rating': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter rating'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter description'}),
            'ordercount': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter ordercount'}),
            'category': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter category'}),
        }


class Adduser(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User

        fields = ('username', 'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'})
        }


class Adduserprofile(forms.ModelForm):
    class Meta:
        model = userinfo
        fields = ('address','phonenumber')
        widgets = {
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Address'}),
            # 'wallet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter wallet'}),
            'phonenumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phonenumber'}),
        }


class Add_delivaryinfo(forms.ModelForm):
    class Meta:
        model = userinfo
        fields = ('address', 'phonenumber')
        widgets = {
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Address'}),
            'phonenumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phonenumber'}),
        }


class Loginform(forms.Form):
    username = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'})
    )
    password = forms.CharField(
        max_length=75,
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'})
    )


class ReviewratingForm(forms.ModelForm):
    class Meta:
        model = Itemreviews
        fields = ('reviews', 'rating')
        widgets = {
            'reviews': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Review:'}),
        }


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('Name_on_card', 'cardno', 'cvv')
        widgets = {
            'Name_on_card': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name_on_card'}),
            'cardno': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Cardno'}),
            'cvv': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter cvv'}),
        }
