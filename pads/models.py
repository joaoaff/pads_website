from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    cargo = models.CharField(max_length=50) # {professor; aluno de graduacao/mestrado/doutorado; visitante; administrador da rede}
    status = models.CharField(max_length=50) # {ativo; aposentado; ex-aluno}
    
class Equipamento(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    manual = models.URLField(max_length=200)
    
class Publicacao(models.Model):
    autor = models.ForeignKey(Usuario)
    outros_autores = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=50) # {TCC; tese de doutorado; dissertacao de mestrado; ...}
    url = models.URLField(max_length=200)