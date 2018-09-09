from django.db import models

# Create your models here.


class Word(models.Model):
    word = models.CharField(max_length=200, verbose_name='Palabra sin traducir')
    word_translated = models.CharField(max_length=200, verbose_name='Palabra traducida')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')


class Dict(models.Model):
    words = models.ManyToManyField(Word)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')