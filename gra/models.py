#-*- coding: utf-8 -*-
#import self as self
from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nazwa")
    published = models.DateTimeField(verbose_name="Data publikacji")
    author= models.CharField(max_length=150,verbose_name="Autor")
    game = models.FileField(upload_to="games", verbose_name="Gra")

    def __unicode__(self):
        return self.name