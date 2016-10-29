from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from models import User
# Create your views here.
def index(request):
    return render(request, 'login_reg_app/index.html')

def login(request):
    if request.method=='POST':
        result = User.objects.validateLogin(request)
        if result[0] == False:
            messages.error(request, result[1], extra_tags='login')
            print_messages(request, result[1])
            return redirect('/')
        return log_user_in(request, result[1])
    else:
        return redirect('/')

def register(request):
    result = User.objects.validateReg(request)

    if result[0] == False:
        print_messages(request, result[1])
        return redirect('/')

    return log_user_in(request, result[1])

def success(request):
    if not 'user' in request.session:
        return redirect('/')

    return redirect('/')
# Change this code
def print_messages(request, message_list):
    for message in message_list:
        messages.add_message(request, messages.INFO, message)

def log_user_in(request, user):
    request.session['user'] = {
        'id' : user.id,
        'name' : user.name,
        'uname' : user.uname
    }
    return redirect('/')

def logout(request):
    request.session.pop('user')
    return redirect('/')
