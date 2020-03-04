from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from chatt.forms import UserLoginForm
from django.contrib.auth.models import User
# from django.db.transaction import connections
from django.contrib.auth.decorators import login_required
# @login_required(login_url='/login')
from django.db.transaction import connections
from chatterbot.ext.django_chatterbot.models import Statement

# Create your views here.
def userRegistration(request):
    if request.user.username:
        return redirect(dashBoard)
    form = UserCreationForm()
    message=''
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = User()
            user.username = username
            user.set_password(password)
            user.save()
            message='User:' + username + 'registration successful '
    return render(request, 'register.html', {'form':form, 'msg': message})


def userLogin(request):
    if request.user.username:
        return redirect(dashBoard)

    form = UserLoginForm()
    message = ''
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            # print(username)
            password = form.cleaned_data['password']
            # print(password)
            user = authenticate(
                username=username,
                password=password
            )

        if user is None:
                message = 'invalid login details'
        else:
                login(request, user)
                # request.session['college_city'] ='bangalore'
                # request.session['college_address']= 'btm'
                return redirect(dashBoard)
    return render(request, 'login.html', {'form': form, 'msg': message})
#


def dashBoard(request):
    return render(request, 'dash.html')


def userLogout(request):
    logout(request)
    return redirect(dashBoard)

@login_required(login_url = '/login')
def data_from_chatbot(request):
    data_list = Statement.objects.all()
    return render(request, "data_db.html", {'datas': data_list})
