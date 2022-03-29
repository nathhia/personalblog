from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=300, null=True, blank=True)
    user = models.ForeignKey("User", on_delete=models.SET_NULL, null=True)
    tag = models.ForeignKey("Tag", on_delete=models.SET_NULL, null=True)
    enabled = models.BooleanField(null=False, blank=False, default=True)
    body = models.CharField(max_length=6000, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)