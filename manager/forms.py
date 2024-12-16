from django import forms

class KeyForms(forms.Form):
    Key = forms.CharField(required=True)
    BookFormId = forms.CharField(required=True)