from django.db import models


class PostManager(models.Manager):

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(published=True)
