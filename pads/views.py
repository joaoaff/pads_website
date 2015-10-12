from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
def main_pt(request):
    return render(request, 'pads/main_pt.html')

def equipe(request):
    return HttpResponse("Essa e a pagina da equipe.")

def atividades(request):
    return HttpResponse("Essa e a pagina de atividades.")

def publicacoes(request):
    return HttpResponse("Essa e a pagina de publicacoes.")

def contato(request):
    return HttpResponse("Essa e a pagina de contato.")