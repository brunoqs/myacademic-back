from django.db import models

from .choices import STUDENT_ROLE
from project.models import Project
from study_group.models import StudyGroup


class Student(models.Model):
    name = models.CharField("Nome", max_length=100)
    role = models.IntegerField(choices=STUDENT_ROLE)
    project = models.ManyToManyField(Project)
    study_group = models.ManyToManyField(StudyGroup)

    def __str__(self):
        return self.name
