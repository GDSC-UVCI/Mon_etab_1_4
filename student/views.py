from django.shortcuts import render
app_name = "student"
# Create your views here.

def index(request):
    return render(request, 'student/three.html', )

def student_add(request):
    return render(request, 'student/four.html')

def student_update(request):
    return render(request, 'student/five.html')