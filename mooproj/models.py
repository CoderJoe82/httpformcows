from django.db import models

class Cow(models.Model):
    text = models.CharField(max_length=80)