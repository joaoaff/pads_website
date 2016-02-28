from django.shortcuts import render
from django.http import HttpResponse

from .models import Equipamento, Usuario

# Create your views here.

# def index(request):
def main_pt(request):
    return render(request, 'pads/main_pt.html')

def equipe(request):
    professor_lista = Usuario.objects.filter(cargo__cargo__startswith='professor')
    aluno_lista = Usuario.objects.filter(cargo__cargo__startswith='aluno')
    context = {'professor_lista': professor_lista,
               'aluno_lista': aluno_lista,}
    return render(request, 'pads/equipe_pt.html', context)

def atividades(request):
    return HttpResponse("Essa e a pagina de atividades.")

def publicacoes(request):
    return HttpResponse("Essa e a pagina de publicacoes.")

def equipamentos(request):
    equipamento_lista = Equipamento.objects.order_by('-categoria')
    context = {'equipamento_lista': equipamento_lista,}
    return render(request, 'pads/equipamentos_pt.html', context)

def contato(request):
    return HttpResponse("Essa e a pagina de contato.")