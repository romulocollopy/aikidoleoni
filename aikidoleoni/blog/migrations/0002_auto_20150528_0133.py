# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('bio', ckeditor.fields.RichTextField(blank=True, verbose_name='Biografia')),
                ('slug', models.SlugField(null=True)),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='Foto', null=True)),
                ('phone', models.CharField(blank=True, max_length=13, verbose_name='Telefone')),
                ('website', models.URLField(blank=True, verbose_name='Site pessoal')),
                ('published', models.BooleanField(choices=[(False, 'em rascunho'), (True, 'publicado')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(related_name='author_user', to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='Título')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Conteudo'),
        ),
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 5, 28, 1, 33, 17, 351625, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Imagem de destaque', null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 28, 1, 33, 26, 975341, tzinfo=utc), verbose_name='Data de Publicação'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=False, choices=[(False, 'em rascunho'), (True, 'publicado')]),
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='Post', max_length=140, verbose_name='Título'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 5, 28, 1, 33, 49, 61749, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='post',
            field=models.ManyToManyField(to='blog.Post'),
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, to='blog.Author'),
        ),
    ]
