from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

def signup_view(request):
    if request.method == 'POST':
        form= UserCreationForm(request.POST)
        if form.is_valid():
            # save() user dönüyor. onu login yapıyoruz
            user = form.save()
            #LOGIN
            login(request,user)
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # form dan user'ı alıyorum
            user = form.get_user()
            #LOGIN
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')


