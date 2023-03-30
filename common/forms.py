from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일") # 기본적으로 필수값이 아닌데 필수값으로 받으려고 입력(meta 클래스 위)

    class Meta:
        model = User
        fields = ("username", "email")