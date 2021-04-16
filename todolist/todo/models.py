from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255)
    check = models.BooleanField(default=False)
    create_dt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title