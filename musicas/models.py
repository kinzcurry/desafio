from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Musica(models.Model):
    nome = models.CharField(max_length=255)
    nome2 = models.CharField(max_length=255, blank=True)
    nome3 = models.CharField(max_length=255, blank=True)
    nome4 = models.CharField(max_length=255, blank=True)
    musica = models.FileField(upload_to='media/')
    imagem = models.ImageField(upload_to='media/imgs/', blank=True)
    tipo = models.CharField(max_length=255)
    fase = models.IntegerField()
    dica = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.nome

class UserResps(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    respostas_lista = models.ForeignKey(Musica, on_delete=models.DO_NOTHING)
    acertou = models.BooleanField(default=False)

    def __str__(self):
        return str(self.usuario)


class UserDicas(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fase = models.CharField(max_length=255, blank=True)
    qtd_dicas = models.IntegerField()
    pontuacaotema = models.IntegerField()

    def __str__(self):
        return str(self.usuario)
