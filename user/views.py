from django.shortcuts import render

# Create your views here.
def user_list(request):
    return render(request, 'user/eleven.html')

def user_add(request):
    return render(request, 'user/twelve.html')

def user_update(request):
    return render(request, 'user/thirteen.html')

def login_user(request):
    return render(request, 'user/login.html')