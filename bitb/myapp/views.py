from django.shortcuts import render
from .forms import LoginForm
from .models import User
from django.shortcuts import redirect
from . import login_eclass 
# Create your views here.

def home_view(request):
    return render(request, 'myeclass.html')

def success_view(request):
    return render(request, 'success.html')

def dongguk_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['userID']
            password= form.cleaned_data['userPW']
            #print(username, password)
            if login_eclass.eclass_confirm(username,password):
                #print("successed login")
                user = User(userID=username, userPW=password)
                user.save()
                print("insert database")
                return redirect('success')
            form = LoginForm()
            return render(request, 'dongguk.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'dongguk.html', {'form': form})

    #return render(request, 'dongguk.html')

def myeclass(request):
    return render(request, 'myeclass.html')
