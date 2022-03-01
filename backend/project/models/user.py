from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False)
    email = models.CharField(max_length=50, null=False, blank=False)
    username = models.CharField(max_length=30, null=False, blank=False)
    moderator = models.BooleanField()
    date_joined = models.DateTimeField(default=timezone.now)
    password = models.CharField(max_length=30, null=False, blank=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['email'], name='Restricao de email'),
            models.UniqueConstraint(fields=['username'], name='Restricao de nome de usuario')
        ]

# Create your models here.
