from django.db import models


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.PROTECT, blank=True, null=True, default=None, related_name='children')

    def __str__(self) -> str:
        return self.name
