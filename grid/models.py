import uuid
from django.db import models
from django.contrib.auth.models import User


class GridElement(models.Model):
    grid = models.ForeignKey("Grid", on_delete=models.CASCADE)
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self) -> str:
        return "{}-{}".format(self.grid.name, self.id)


class Grid(models.Model):
    name = models.CharField(max_length=32, default="FirstGrid")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
