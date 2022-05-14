from django.contrib import admin

from .models import Cargo, Trab, Funcionario, RecursoDireita, RecursoEsquerda, Precos
# Register your models here.


@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo', 'editado')


@admin.register(Trab)
class TrabAdmin(admin.ModelAdmin):
    list_display = ('trab', 'icone', 'ativo', 'editado')


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'ativo', 'editado')


@admin.register(RecursoDireita)
class RecursoDAdmin(admin.ModelAdmin):
    list_display = ('recurso_direita', 'icone', 'ativo', 'editado')


@admin.register(RecursoEsquerda)
class RecursoEAdmin(admin.ModelAdmin):
    list_display = ('recurso_esquerda', 'icone', 'ativo', 'editado')


@admin.register(Precos)
class PrecosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'icone', 'ativo', 'editado')