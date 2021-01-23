from django.db import models
from core import models as core_models

# Create your models here.


class Note(core_models.TimeStampedModel):
    title = models.CharField(max_length=120)
    text = models.TextField()
