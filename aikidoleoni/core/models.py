from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


# Create your models here.
class Page(models.Model):
    title = models.CharField(_('Titulo'), max_length=140)
    slug = models.SlugField(unique=True)
    description = models.CharField(_('Descrição'),max_length=140, blank=True)
    content = models.TextField(_('Conteúdo'),blank=True)
    image = models.ImageField(_('Imagem de destaque'),
                              upload_to="cover_images",blank=True)
    created_at=models.DateTimeField(_('Criado em'),auto_now_add=True)
    updated_at=models.DateTimeField(_('Atualizado em'), auto_now=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return self.slug
