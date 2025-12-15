from django.db import models
import uuid

from diplome.models import Diplome

from categorie.models import SousCategorie


# Create your models here.
class OffreRecrutement(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    categorie = models.ForeignKey(SousCategorie, on_delete=models.CASCADE)

    libelle = models.CharField(max_length=500, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.libelle


class OffreDiplome(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    diplome = models.ForeignKey(Diplome, on_delete=models.CASCADE)
    offre = models.ForeignKey(OffreRecrutement, on_delete=models.CASCADE)

    libelle = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True, null=True)


class Postule(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    offre = models.ForeignKey(OffreRecrutement, on_delete=models.CASCADE)
    diplome = models.ForeignKey(Diplome, on_delete=models.CASCADE)

    nom = models.CharField(max_length=500, null=False, blank=False)
    prenom = models.CharField(max_length=500, null=False, blank=False)
    lieu_n = models.CharField(max_length=500, null=False, blank=False)
    zone = models.CharField(max_length=500, null=False, blank=False)
    image = models.ImageField(null=True, blank=True)

    carte_i = models.FileField(null=True, blank=True)
    diplome_pdf = models.FileField(null=True, blank=True)

    date_n = models.DateTimeField(auto_now_add=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nom


class TypeEpreuve(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    libelle = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True, null=True)


class Epreuve(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    type = models.ForeignKey(TypeEpreuve, on_delete=models.CASCADE)
    diplome = models.ForeignKey(Diplome, on_delete=models.CASCADE)

    statut = models.CharField(max_length=500, null=False, blank=False)
    note = models.IntegerField(default=0)

    date_e = models.DateTimeField(auto_now_add=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)

