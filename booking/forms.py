from django import forms


class BookForms(forms.Form):
    ServerRoomName = forms.CharField(required=True)
    ApplicantName = forms.CharField(required=True)
    Mobile = forms.CharField(required=True)
    Email = forms.CharField(required=False)