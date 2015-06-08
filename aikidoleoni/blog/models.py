from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

from aikidoleoni.blog.managers import PostManager

PUBLISHED = (
    (False, 'em rascunho'),
    (True, 'publicado')
    )


class Author(models.Model):
    user = models.OneToOneField(User, null=True, related_name='author_user')
    bio = RichTextField(_('Biografia'), blank=True)
    slug = models.SlugField(null=True)
    image = models.ImageField(_('Foto'), blank=True, null=True)
    phone = models.CharField(_('Telefone'), max_length=13, blank=True)
    website = models.URLField(_('Site pessoal'), blank=True)
    published = models.BooleanField(choices=PUBLISHED)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.user.first_name:
            return '{} {}'.format(self.user.first_name, self.user.last_name)
        return self.user.username


class Post(models.Model):
    title = models.CharField(_('Título'), max_length=140)
    subtitle = models.CharField(_('Sub Título'), max_length=140, null=True)
    slug = models.SlugField(null=True)
    content = RichTextField(_('Conteudo'), blank=True)
    author = models.ForeignKey(Author, null=True)
    publish_date = models.DateTimeField(_('Data de Publicação'))
    published = models.BooleanField(choices=PUBLISHED, default=False)
    image = models.ImageField(_('Imagem de destaque'), blank=True,
                              null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    published_posts = PostManager()

    def save(self, *args, **kwargs):
        if not self.content:
            self.published = False
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Tag(models.Model):
    post = models.ManyToManyField(Post)
    title = models.CharField(_('Título'), max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.title
