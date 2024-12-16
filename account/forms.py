from django import forms

class LoginForm(forms.Form):
    Account = forms.CharField(required=True) # 账号/工号/手机号
    PassWord = forms.CharField(required=True,min_length=6)