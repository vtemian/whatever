from django.db import models
from django.contrib.auth.models import User
import json
import urllib


class Admin(models.Model):
    user = models.OneToOneField(User)


class Prof(models.Model):
    user = models.OneToOneField(User)
    liceu = models.ForeignKey()