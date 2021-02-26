from django.db import models

# Create your models here.

class Produto (models.Model):
    grupo = models.CharField(max_length=100)
    nome = models.CharField(max_length=100)
    img1 = models.ImageField(upload_to='pics/')
    img2 = models.ImageField(upload_to='pics/', null=True, blank=True)
    img3 = models.ImageField(upload_to='pics/', null=True, blank=True)
    img4 = models.ImageField(upload_to='pics/', null=True, blank=True)
    img5 = models.ImageField(upload_to='pics/', null=True, blank=True)
    img6 = models.ImageField(upload_to='pics/', null=True, blank=True)
    descricao = models.TextField()
    sugestao = models.TextField()