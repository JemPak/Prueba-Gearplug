
from django.db import models
from django.utils.translation import gettext_lazy as _

class Character(models.Model):
    
    resident = models.ForeignKey('resident', on_delete=models.PROTECT)
    films = models.ManyToManyField('film', related_name='films')