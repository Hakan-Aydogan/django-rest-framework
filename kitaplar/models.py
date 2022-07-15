from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.


class Kitap(models.Model):
    yazar = models.CharField(max_length=150)
    isim = models.CharField(max_length=150)
    aciklama = models.TextField(max_length=5000)
    yaratilma_tarihi = models.DateTimeField(auto_now_add=True)
    güncellenme_tarihi = models.DateTimeField(auto_now=True)
    yayinlanma_tarihi = models.DateField()

    def __str__(self):
        return f'{self.yazar} - {self.isim}'


class Yorum(models.Model):
    kitap = models.ForeignKey(
        Kitap, on_delete=models.CASCADE, related_name='yorumlar')
    yorum_sahibi = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='yorum_yapan')
    yorum = models.TextField(max_length=1000)
    yaratilma_tarihi = models.DateTimeField(auto_now_add=True)
    güncellenme_tarihi = models.DateTimeField(auto_now=True)

    degerlendirme = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f'{self.degerlendirme}'
