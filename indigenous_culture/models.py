from django.db import models
from translate.models import Dict

# Create your models here.
class Culture(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    image = models.ImageField(verbose_name='Imagen', upload_to='culture_images/')
    description = models.TextField(verbose_name='Descripcion')
    dict = models.OneToOneField(Dict, on_delete=models.CASCADE)
