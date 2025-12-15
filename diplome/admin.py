from django.contrib import admin

from .models import Diplome


# Register your models here.
@admin.register(Diplome)
class AdminDiplome(admin.ModelAdmin):
    ...

