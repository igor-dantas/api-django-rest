from rest_framework import viewsets
from Noticia.api import serializers
from Noticia import models
class noticiasViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.noticiasSerializer
    queryset = models.noticias.objects.all()