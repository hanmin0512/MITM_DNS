from django import forms

class LoginForm(forms.Form):
    userID = forms.CharField(label='아이디', max_length=255)
    userPW = forms.CharField(label='비밀번호', widget=forms.PasswordInput)

