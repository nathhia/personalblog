from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False)
    user = models.ForeignKey("User", on_delete=models.SET_NULL, null=True)
    enabled = models.BooleanField(null=False, blank=False, default=True)