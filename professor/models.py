from django.db import models
from django.conf import settings


class Professor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    educational_background = models.TextField()
    room = models.CharField("Sala", max_length=50)
    phone = models.CharField("Telefone", max_length=50)

    def __str__(self):
        return self.user.get_full_name()
