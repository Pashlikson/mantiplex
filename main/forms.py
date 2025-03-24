from django import forms
from main.models.role import Role

class ProfileForm(forms.Form):
    first_name = forms.CharField(label='Your name', max_length=100)
    last_name = forms.CharField(label='Your last name', max_length=100)
    email = forms.EmailField(label='Your email', max_length=100)
    role = forms.ModelChoiceField(
        queryset=Role.objects.all()
    )
    birth_date = forms.DateField(label='Your birth day')