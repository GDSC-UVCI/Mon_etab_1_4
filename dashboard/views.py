from django.shortcuts import render

# Create your views here.
def report(request):
    return render(request, 'dashboard/thirteen.html')

def index(request):
    return render(request, 'dashboard/index.html')