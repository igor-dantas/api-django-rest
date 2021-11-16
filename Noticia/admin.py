from django.contrib import admin
from Noticia.models import noticias

class Noticia(admin.ModelAdmin):
    list_display = ('id_not', 'titulo', 'conteudo', 'autor', 'publicado', 'data_criacao')
    list_display_links = ('id_not',)
    search_fields = ('id_not', 'titulo',)
admin.site.register(noticias, Noticia)