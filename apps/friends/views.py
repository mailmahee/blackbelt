from django.shortcuts import render, redirect
from models import Friendship

# Create your views here.
def index(request):
    return redirect('/main')

def main(request):
    if 'user' in request.session:
        return redirect('/friends')
    else:
        return render(request,'login_reg_app/index.html')

def show_friends(request):
    context = Friendship.objects.get_complete_context(request)
    if 'user' in request.session:
        return render(request,'friends/index.html',context)
    else:
        return redirect('/main')

def view_profile(request,id):
    context = Friendship.objects.view_profile(request,id=id)
    if 'user' in request.session:
        return render(request,'friends/viewProfile.html',context)
    else:
        return redirect('/main')

def add_friend(request,id):
    if 'user' in request.session:
        response = Friendship.objects.add_friend(request,id=id)
        print response
        return redirect('/main')
    else:
        return redirect('/main')

def remove_friend(request,id):
    if 'user' in request.session:
        response = Friendship.objects.remove_friend(request,id=id)
        print response
        return redirect('/main')
    else:
        return redirect('/main')
