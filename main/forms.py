from django import forms
from main.models.role import Role as Role_queryset

class ProfileForm(forms.Form):
    first_name = forms.CharField(label='Your name', max_length=100)
    last_name = forms.CharField(label='Your last name', max_length=100)
    email = forms.EmailField(label='Your email', max_length=100)
    role = forms.ModelChoiceField(
        queryset=Role_queryset.objects.all()
    )
    # поле з датою народження має бути віджетом з валідацією: max_date < today and min_date >= today - 90 років
    birth_date = forms.DateField(label='Your birth day')