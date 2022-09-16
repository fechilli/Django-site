from django.shortcuts import render
from django.http import HttpResponse
from .models import Transacao
import datetime


def home(request):
    data = {}
    data['now'] = datetime.datetime.now()
    data['transacoes'] =['t1', 't2',' t3', 'a1', 'a2','q3']

    return render(request, 'contas/home.html', data)

def Listagem (request):
    data = {}
    data['transacoes'] = Transacao.objets.all()
    return render(request, 'contas/listagem.html')