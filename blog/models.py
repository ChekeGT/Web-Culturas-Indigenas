from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name='Nombre')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')

    class Meta:
        ordering = ['name']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='Titulo')
    image = models.ImageField(upload_to='post_images/',verbose_name='Imagen')
    content = models.TextField(verbose_name='Contenido')
    categories = models.ManyToManyField(Category)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')

    class Meta:
        ordering = ['title']
        verbose_name = 'Publicacion'
        verbose_name_plural = 'Publicaciones'

    def __str__(self):
        return  self.title


class Blog(models.Model):
    posts = models.ManyToManyField(Post)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')

    class Meta:
        ordering = ['updated']
        verbose_name_plural = 'Blogs'
        verbose_name = 'Blog'

    def __str__(self):
        return 'Blog Numero: {}'.format(self.pk)
