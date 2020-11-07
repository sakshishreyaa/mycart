
from django import forms
from models import *

class CustomerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = ('user_id','name', 'email', 'password', 'house_no', 'address_line1', 'address_line2', 'telephone', 'zip_code', 'state', 'country')