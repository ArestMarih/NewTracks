from django.db import models

class quest(models.Model):
    nameQu = models.CharField(max_length=128)
    comments = models.TextField(null=True,blank=True)
    exp = models.PositiveIntegerField(default=0)
    done = models.BooleanField(default=False)