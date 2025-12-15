from django.db import models
import uuid

# Create your models here.
class Categorie(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    libelle = models.CharField(max_length=500, null=False, blank=False)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.libelle

    @property
    def sous_categorie(self):
        return self.souscategorie_set.all()

    

class SousCategorie(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    libelle = models.CharField(max_length=200)
    
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    @property
    def all_entrer(self):
        return self.entrer_set.all()
