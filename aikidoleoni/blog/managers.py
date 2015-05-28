from django.db import models
from django.utils import timezone

class PostManager(models.Manager):

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(
            published=True,
            publish_date__lte=timezone.now()
            )
        return qs
