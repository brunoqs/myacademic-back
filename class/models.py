from django.db import models

from .choices import CLASS_TYPE


class Class(models.Model):
    name = models.CharField("Disciplina", max_length=50)
    type = models.IntegerField(choices=CLASS_TYPE)

    def __str__(self):
        return self.name


class ClassContent(models.Model):
    fk = models.ForeignKey('Class', on_delete=models.DO_NOTHING)
    content = models.FileField(upload_to='contents/')
