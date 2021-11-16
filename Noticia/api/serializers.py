from rest_framework import serializers
from Noticia import models

class noticiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.noticias
        fields = '__all__'