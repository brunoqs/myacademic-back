from django.db import models


class StudyGroup(models.Model):
    name = models.CharField("Nome", max_length=100)

    def __str__(self):
        return self.name
