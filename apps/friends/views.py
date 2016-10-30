from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return redirect('/main')

def main(request):
    if 'user' in request.session:
        return redirect('/friends')
    else:
        return render(request,'login_reg_app/index.html')

def show_friends(request):
    if 'user' in request.session:
        return render(request,'friends/index.html')
    else:
        return redirect('main')

def view_profile(request,id):
    if 'user' in request.session:
        return render(request,'friends/viewProfile.html')
    else:
        return redirect('main')
