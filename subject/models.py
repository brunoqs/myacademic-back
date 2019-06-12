from django.db import models

from .choices import SUBJECT_TYPE


class Subject(models.Model):
    name = models.CharField("Disciplina", max_length=50)
    type = models.IntegerField(choices=SUBJECT_TYPE)

    def __str__(self):
        return self.name


class SubjectContent(models.Model):
    fk = models.ForeignKey('Subject', related_name='contents', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    content = models.FileField(upload_to='contents/')

    def __str__(self):
        return self.title
