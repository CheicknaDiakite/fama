from django.db import models
import uuid
# Create your models here.
class Diplome(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    libelle = models.CharField(max_length=500, null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.libelle

