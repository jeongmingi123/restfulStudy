from django.db import models
from core.models import TimeStampModel

class Blog(TimeStampModel):

    title = models.CharField(max_length=30)
    text = models.TextField()
    comment = models.CharField(max_length=60)

    def __str__(self):
        return self.title
