from django.db import models


class Todo(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.name