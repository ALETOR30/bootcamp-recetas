from django.shortcuts import render


def registro(request):
    contexto = {}
    return render(request, "user/registro.html", contexto)