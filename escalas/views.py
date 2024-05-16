from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import funcionario
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


def home (request):
    return render(request,"pagina_inicial.html")

def tela_login(request):
    return render(request,"tela_inicial.html")

class FuncionarioListView(ListView):
  model = funcionario


class FuncionarioCreateView(CreateView):
    model = funcionario
    fields =['Nome','Sobrenome','Registro_Empresa','Escala_de_trabalho']
    success_url = reverse_lazy("lista")


class FuncionarioUpdateView(UpdateView):
    model = funcionario
    fields =['Nome','Sobrenome','Registro_Empresa','Escala_de_trabalho']
    success_url = reverse_lazy("lista")


class FuncionarioDeleteView(DeleteView):
    model = funcionario
    success_url = reverse_lazy("lista")
    