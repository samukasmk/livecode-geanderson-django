from django.contrib import admin
from django.contrib import messages


from .models import Pessoa, AnalisePessoasCSV

# Register your models here.

class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome_e_sobrenome', 'logradouro', 'num_casa')
    pass


    def nome_e_sobrenome(self, obj):
        return obj.nome + ' ' + obj.sobrenome


def analise_qtd_pessoas(modeladmin, request, queryset):
    analises_solicitadas = queryset.all()
    for analise in analises_solicitadas:
        qtd_pessoas = sum(1 for row in analise.csv_file)
        messages.info(request, 'Qtd de pessoas contadas: ' + str(qtd_pessoas) + ' no arquivo csv: ' + str(analise.csv_file.name))

analise_qtd_pessoas.short_description = "Conta quantas linhas tem no CSVs"


class AnalisePessoasCSVAdmin(admin.ModelAdmin):
    actions = [analise_qtd_pessoas]






admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(AnalisePessoasCSV, AnalisePessoasCSVAdmin)






#
# class Admin(admin.ModelAdmin):
#     '''
#         Admin View for
#     '''
#     list_display = ('',)
#     list_filter = ('',)
#     inlines = [
#         Inline,
#     ]
#     raw_id_fields = ('',)
#     readonly_fields = ('',)
#     search_fields = ('',)
#
#
# admin.site.register(, Admin)
