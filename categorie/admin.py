from django.contrib import admin

from .models import Categorie, SousCategorie


# Register your models here.
@admin.register(Categorie)
class AdminCategorie(admin.ModelAdmin):
    ...


@admin.register(SousCategorie)
class AdminSousCategorie(admin.ModelAdmin):
    ...