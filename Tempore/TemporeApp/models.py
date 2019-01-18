from django.db import models
from django.contrib.auth.models import User


class person(models.Model):
        name = models.TextField