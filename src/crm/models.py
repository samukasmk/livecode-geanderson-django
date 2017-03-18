from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    sobrenome = models.CharField(max_length=200)
    logradouro = models.CharField(max_length=255)
    num_casa = models.IntegerField()

    def __str__(self):
        return self.nome


class AnalisePessoasCSV(models.Model):
    csv_file = models.FileField(upload_to='uploads_csv/%Y/%m/%d/')

    def __str__(self):
        return 'Analise #' + str(self.id)