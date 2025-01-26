from django.db import models

# Create your models here.

class Artigo(models.Model):
    titulo = models.CharField(max_length=60)
    conteudo = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
