from django.db import models
from django.conf import settings


class Link(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, default=None)
    name = models.CharField(max_length=100, unique=True)
    target = models.URLField()

    def __str__(self):
        return "<Link '%s' to '%s'>" % (self.name, self.target)
