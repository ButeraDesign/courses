from django.shortcuts import render, HttpResponse, redirect
from .models import Courses

def index(request):
    allCourses = Courses.objects.all()
    context = {
        'courseList' : allCourses
    }
    return render(request, 'coursesApp/index.html', context)

def delete(request):
    if request.method == "POST":
        id = request.POST['id']
        course = Courses.objects.get(pk=id)
        course.delete()
        return redirect('/');

def deleteQuestion(request, id):
    course = Courses.objects.get(pk=id)
    context = {
        'name' : course.name,
        'discription' : course.discription,
        'id': id
    }

    return render(request, 'coursesApp/delete.html', context)


def add(request):

    if request.method == "POST":

        Courses.objects.create(name=request.POST['name'], discription=request.POST['discription'])
        return redirect('/');
