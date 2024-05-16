
from django.contrib import admin
from django.urls import path,include
from escalas.views import  home,tela_login
from escalas.views import FuncionarioListView,FuncionarioCreateView,FuncionarioUpdateView,FuncionarioDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tela_login),
    path('pagina_inicial',home),
    path('escala', FuncionarioListView.as_view(), name = "lista"),
    path('cadastro',FuncionarioCreateView.as_view(), name='cadastro'),
    path('atualizar/<int:pk>',FuncionarioUpdateView.as_view(),name ='atualizar'),
    path('deletar/<int:pk>',FuncionarioDeleteView.as_view(),name ='deletar'),
    path('accounts/',include('django.contrib.auth.urls'), name='login'),
]
