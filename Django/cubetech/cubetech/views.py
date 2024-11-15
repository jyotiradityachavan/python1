from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    data = {
        'title': 'Home Page 1',
        'bdata': 'Welcome to Cubetech',
        'clist': ['php', 'java', 'django'],
        'numbers': [10, 20, 30, 40, 50],
        'student_details': [
            {'name': 'aditya', 'phone': 8766447176},
            {'name': 'ankit', 'phone': 9962014576}
        ]
    }
    return render(request, "index.html", data)

def aboutUS(request):
    return HttpResponse("Welcome to wscubetech")

def course(request):
    return HttpResponse("Welcome to wscubetech1")

def courseDetails(request, courseid):
    return HttpResponse(f"Course ID: {courseid}")
