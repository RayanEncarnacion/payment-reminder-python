from django import forms

class CreateClient(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()