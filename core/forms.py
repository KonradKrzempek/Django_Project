from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True, help_text="Required. Insert a valid email address")
    date_of_birth = forms.DateField(input_formats='%d/%m/%Y', help_text="DD/MM/YYYY format")
    street = forms.CharField(max_length=50)
    post_code = forms.CharField(max_length=20)
    city = forms.CharField(max_length=30)
    country = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'date_of_birth', 'email',
                  'street', 'city', 'post_code', 'country')
