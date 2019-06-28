from django.db import models


class Project(models.Model):
    name = models.CharField("Nome", max_length=50)
    abstract = models.TextField("Resumo")
    year_beg = models.DateField()
    year_end = models.DateField()
    paper = models.FileField(upload_to='papers/')

    def __str__(self):
        return self.name
