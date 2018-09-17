from django.db import models

# Create your models here.

class Word(models.Model):
    word = models.CharField(max_length=200, verbose_name='Palabra sin traducir')
    word_translated = models.CharField(max_length=200, verbose_name='Palabra traducida')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')
    class Meta:
        ordering = ['word', 'word_translated']
        verbose_name_plural = 'Palabras'
        verbose_name = 'Palabra'

    def __str__(self):
        return self.word


class Dict(models.Model):
    words = models.ManyToManyField(Word)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')
    class Meta:
        ordering = ['created']
        verbose_name = 'Diccionario'
        verbose_name_plural = 'Diccionarios'


class Culture(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    image = models.ImageField(verbose_name='Imagen', upload_to='culture_images/')
    image_description = models.CharField(max_length=200, verbose_name='Descripcion de imagen')
    description = models.TextField(verbose_name='Descripcion')
    dict = models.OneToOneField(Dict, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')

    class Meta:
        ordering = ['name']
        verbose_name = 'Cultura Indigena'
        verbose_name_plural = 'Culturas Indigenas'

    def __str__(self):
        return self.name