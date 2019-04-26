from django.db import models


class Project(models.Model):
    name = models.CharField("Nome", max_length=50)
    abstract = models.TextField("Resumo")
    year_beg = models.IntegerField()
    year_end = models.IntegerField()
    paper = models.FileField(upload_to='papers/')

    def __str__(self):
        return self.name
