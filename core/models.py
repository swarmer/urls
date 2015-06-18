from django.db import models


class Link(models.Model):
    name = models.CharField(max_length=100, unique=True)
    target = models.URLField()

    def __str__(self):
        return "<Link '%s' to '%s'>" % (self.name, self.target)
