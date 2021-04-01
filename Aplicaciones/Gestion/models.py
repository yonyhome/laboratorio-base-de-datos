from django.db import models

# Create your models here.
class Padre(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=20)
    def __str__(self):
        return self.nom

class Hijo(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=20)
    hijode = models.ForeignKey(Padre, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom
