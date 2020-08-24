from django.db import models


class GridElement(models.Model):
    grid = models.ForeignKey("Grid", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return "{}-{}".format(self.grid.name, self.id)


class Grid(models.Model):
    name = models.CharField(max_length=32, default="FirstGrid")

    def __str__(self) -> str:
        return self.name
