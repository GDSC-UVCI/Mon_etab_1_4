from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'teacher/seven.html')

def teacher_add(request):
    return render(request, 'teacher/eight.html')

def teacher_update(request):
    return render(request, 'teacher/nine.html')

