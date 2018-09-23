from django.db import models
from django.dispatch import receiver
from translate.models import Dict
from blog.models import Blog
from django.db.models.signals import pre_save, post_delete
# Create your models here.



class Culture(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    image = models.ImageField(verbose_name='Imagen', upload_to='culture_images/')
    image_description = models.CharField(max_length=200, verbose_name='Descripcion de imagen')
    description = models.TextField(verbose_name='Descripcion')
    dict = models.OneToOneField(Dict, on_delete=models.CASCADE, null=True, blank=True)
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')

    class Meta:
        ordering = ['name']
        verbose_name = 'Cultura Indigena'
        verbose_name_plural = 'Culturas Indigenas'

    def __str__(self):
        return self.name


@receiver(pre_save, sender=Culture)
def ensure_dict_is_created(sender, instance, **kwargs):
        if instance.dict == None:
            instance.dict = Dict.objects.create()
        if instance.blog == None:
            instance.blog = Blog.objects.create()
        if 'cultura' in instance.name.lower():
            instance.name = instance.name.lower().replace('cultura', '')
            instance.name = instance.name.capitalize()

@receiver(post_delete, sender=Culture)
def ensure_dict_and_their_words_are_deleted_(sender, instance, *args, **kwargs):
    for word in instance.dict.words.all():
        word.delete()
    instance.blog.delete()
    instance.dict.delete()


