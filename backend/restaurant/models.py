from django.db import models


class Restaurant(models.Model):
    title = models.CharField(max_length=32)
    menu = models.ForeignKey('menu.Menu', on_delete=models.DO_NOTHING, blank=True)

    def __str__(self):
        return self.title
