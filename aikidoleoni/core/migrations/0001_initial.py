# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=140, verbose_name='Titulo')),
                ('slug', models.SlugField(unique=True)),
                ('description', models.CharField(blank=True, max_length=140, verbose_name='Descrição')),
                ('content', models.TextField(blank=True, verbose_name='Conteúdo')),
                ('image', models.ImageField(blank=True, upload_to='cover_images', verbose_name='Imagem de destaque')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(verbose_name='Atualizado em', auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
