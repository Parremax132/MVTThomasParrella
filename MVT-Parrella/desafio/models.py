from django.db import models

# Create your models here.

class Fam(models.Model):
    nombre=models.CharField(max_length=30)
    edad=models.IntegerField()
    fecha=models.DateField(null=True)
    