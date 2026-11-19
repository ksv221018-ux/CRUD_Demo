from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": "User already exists"})

        User.objects.create_user(
            username=username,
            password=password
        )
        return redirect("login")
    return render(request, "register.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect("insert")
        return render(request, "login.html", {"error": "Invalid username or password"})
    return render(request, "login.html")


def insert_data(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')

        Student.objects.create(
            name=name,
            age=age,
            email=email
        )
        messages.success(request, "Student inserted successfully!")
        return redirect("insert")
    return render(request, "insert.html")

def read_data(request):
    data = Student.objects.all()
    return render(request, "read.html", {"data": data})

def update_data(request, id):
    data = get_object_or_404(Student, id=id)

    if request.method == "POST":
        data.name = request.POST.get('name')
        data.age = request.POST.get('age')
        data.email = request.POST.get('email')
        data.save()
        messages.success(request, "Student updated successfully!")
        return redirect("read")
    return render(request, "update.html", {"data": data})

def delete_data(request, id):
    data = get_object_or_404(Student, id=id)
    if request.method == "POST":
        data.delete()
        messages.success(request, "Student deleted successfully!")
    return redirect("read")

def user_logout(request):
    if request.method == "POST":
        logout(request)
    return redirect("login")
