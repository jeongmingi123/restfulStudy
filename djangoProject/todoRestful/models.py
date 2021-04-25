from django.db import models


# Create your models here.

class TodoRestfulModel(models.Model):
    item = models.CharField(max_length=30, null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)