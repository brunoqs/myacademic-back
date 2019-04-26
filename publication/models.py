from django.db import models

from .choices import PUBLICATION_TYPE


class Publication(models.Model):
    name = models.CharField("Nome", max_length=100)
    type = models.IntegerField(choices=PUBLICATION_TYPE)
    bibtex = models.FileField(upload_to='publications/')

    def __str__(self):
        return self.name
