from django import template
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, response, Http404
from django.template import context, loader

from .models import Type_Movto, Movto

def index(request):
    tipo_movto_list = Type_Movto.objects.order_by('nome')
    context = {
        'tipo_movto_list': tipo_movto_list
    }
    return render(request, 'movto/index.html', context)

def detail(request, id):
    try:
        tipo_movto = Type_Movto.objects.get(id=id)
    except Type_Movto.DoesNotExist:
        raise Http404("Tipo de movimento não existe.")
    
    return render(request, 'movto/detail.html', {'tipo_movto': tipo_movto})


def get_type_movto(request):
    response = Type_Movto.objects.all()
    return HttpResponse(response)


def get_type_movto_id(request, id):
    response = Type_Movto.objects.get(id=id)
    print(response)
    return HttpResponse(response)
