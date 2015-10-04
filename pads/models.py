from django.db import models

# Create your models here.

class Cargo(models.Model):
    cargo = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.cargo
    
class Status(models.Model):
    status = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.status
    
class TipoPub(models.Model):
    tipo = models.CharField(max_length=50)
    
    def __unicode__(self):
        return self.tipo
    
class Categoria(models.Model):
    categoria = models.CharField(max_length=50)
      
    def __unicode__(self):
        return self.categoria

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    cargo = models.ForeignKey(Cargo) # {professor; aluno de graduacao/mestrado/doutorado; visitante; administrador da rede}
    status = models.ForeignKey(Status) # {ativo; aposentado; ex-aluno}
    
    def __unicode__(self):
        return self.nome
    
class Equipamento(models.Model):
    categoria = models.ForeignKey(Categoria)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    manual = models.URLField(max_length=200)
    
    def __unicode__(self):
        return self.modelo
    
class Publicacao(models.Model):
    autor = models.ForeignKey(Usuario)
    outros_autores = models.CharField(max_length=200)
    titulo = models.CharField(max_length=200)
    tipo = models.ForeignKey(TipoPub) # {TCC; tese de doutorado; dissertacao de mestrado; ...}
    url = models.URLField(max_length=200)
    
    def __unicode__(self):
        return self.titulo
    