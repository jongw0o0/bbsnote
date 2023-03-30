from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .forms import UserForm

# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_passward = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_passward)
            login(request, user)
            return redirect('index') # 회원가입 후 메인페이지
            # return redirect('common:login') 회원가입 후 로그인페이지
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form':form}) 