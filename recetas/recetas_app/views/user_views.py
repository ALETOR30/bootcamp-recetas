from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse

def registro(request):
    contexto = {}
    if request.method == "POST":
        print("post")
        username = request.POST.get('username')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_exist = User.objects.filter(username = username).exists()
        if user_exist:
            error = "El usuario ya existe"
            contexto ['error'] = error
            contexto ['nombre'] = nombre
            contexto ['apellido'] = apellido
            contexto ['username'] = username
            contexto ['email'] = email
        else:
            print(" Crear el usuario")
            User.objects.create_user (username, email, password, first_name=nombre, last_name=apellido) 
            url = "{}?greetings=true" .format(reverse('login'))
            return redirect(url)
    else:
        print("get")
    return render(request, "user/registro.html", contexto)

def login(request):
    contexto = {}
    if request.method =="GET":
        greetings =request.GET.get('greetings')
        print ("greetings:{}" .format(greetings))
        if greetings == "true":
            contexto['mensaje'] = "Cuenta creada, autenticate."
    return render(request, "user/login.html", contexto)

