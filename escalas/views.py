from django.shortcuts import render

def home (request):
    return render(request," escalas/pagina_inicial.html")
