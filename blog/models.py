from django.conf import settings
from django.db import models
from django.utils import timezone


class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)

    def __str__(self):
        return "{} {}".format(email, name)

    class Meta:
        verbose_name = "MySubcriber"
        verbose_name_plural = "A lot of Subscribers"
