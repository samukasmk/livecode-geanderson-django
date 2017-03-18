from django.shortcuts import render
from django.http import JsonResponse
from .models import Pessoa

import csv
from django.http import HttpResponse


def get_pessoas_json(request):

    todas_as_pessoas = Pessoa.objects.all()

    pessoas_dict = {}

    for pessoa_localizada_no_bd in todas_as_pessoas:
        pessoas_dict[pessoa_localizada_no_bd.nome] = {
            'nome': pessoa_localizada_no_bd.nome,
            'logradouro': pessoa_localizada_no_bd.logradouro,
            'casa': pessoa_localizada_no_bd.num_casa,
        }

    return JsonResponse(pessoas_dict,
        json_dumps_params={'sort_keys': True})


def get_pessoas_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="pessoas.csv"'
    todas_as_pessoas = Pessoa.objects.all()
    pessoas_csv = csv.writer(response)
    for pessoa_localizada_no_bd in todas_as_pessoas:
        pessoas_csv.writerow([
            pessoa_localizada_no_bd.nome,
            pessoa_localizada_no_bd.logradouro,
            pessoa_localizada_no_bd.num_casa
        ])

    return response