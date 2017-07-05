from django.db import models

# Create your models here.
class Genere(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Movies(models.Model):
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    rel_date = models.DateTimeField()
    genere = models.ForeignKey(Genere,default=1)

    def __str__(self):
        return self.name

