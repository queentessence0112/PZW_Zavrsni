from django.db import models

# Create your models here.

class Odjel(models.Model):
    naziv_odjela = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.naziv_odjela
    

class Pacijent(models.Model):
    broj_zdravstvene = models.CharField(max_length=9, unique=True)
    ime_pacijenta = models.CharField(max_length=50)
    prezime_pacijenta = models.CharField(max_length=50)
    broj_mobitela = models.CharField(max_length=10)
    razlog_dolaska = models.TextField()
    odjel = models.ForeignKey(Odjel, on_delete=models.CASCADE)

    def __str__(self):
        return self.prezime_pacijenta