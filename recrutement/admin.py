from django.contrib import admin

from .models import Postule, Epreuve, TypeEpreuve, OffreDiplome, OffreRecrutement


# Register your models here.
@admin.register(OffreRecrutement)
class AdminOffreRecrutement(admin.ModelAdmin):
    ...


@admin.register(Postule)
class AdminPostule(admin.ModelAdmin):
    ...


@admin.register(OffreDiplome)
class AdminOffreDiplome(admin.ModelAdmin):
    ...


@admin.register(TypeEpreuve)
class AdminTypeEpreuve(admin.ModelAdmin):
    ...


@admin.register(Epreuve)
class AdminEpreuve(admin.ModelAdmin):
    ...

