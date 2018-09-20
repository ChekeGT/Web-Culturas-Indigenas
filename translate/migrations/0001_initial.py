# Generated by Django 2.1.1 on 2018-09-20 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
            ],
            options={
                'verbose_name': 'Diccionario',
                'verbose_name_plural': 'Diccionarios',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=200, verbose_name='Palabra sin traducir')),
                ('word_translated', models.CharField(max_length=200, verbose_name='Palabra traducida')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edicion')),
            ],
            options={
                'verbose_name': 'Palabra',
                'verbose_name_plural': 'Palabras',
                'ordering': ['word', 'word_translated'],
            },
        ),
        migrations.AddField(
            model_name='dict',
            name='words',
            field=models.ManyToManyField(to='translate.Word'),
        ),
    ]