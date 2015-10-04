from django.contrib import admin
from .models import Cargo, Status, TipoPub, Categoria, Usuario, Equipamento, Publicacao

# Register your models here.

admin.site.register(Cargo)
admin.site.register(Status)
admin.site.register(TipoPub)
admin.site.register(Categoria)
admin.site.register(Usuario)
admin.site.register(Equipamento)
admin.site.register(Publicacao)