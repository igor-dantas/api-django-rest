from django.db import models
from uuid import uuid4

class noticias(models.Model):
    id_not = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    titulo = models.CharField(max_length=255)
    conteudo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    publicado = models.BooleanField()
    data_criacao = models.DateField(auto_now_add=True)