from django.db import models

class quest(models.Model):
    nameQu = models.CharField(max_length=128)
    comments = models.TextField(null=True,blank=True)
    exp = models.PositiveIntegerField(default=0)
    done = models.BooleanField(default=False)

class Person(models.Model):
    exp = models.PositiveIntegerField()

class Lvlvs(models.Model):
    minExp = models.PositiveIntegerField()
    maxExp = models.PositiveIntegerField()
    title = models.CharField()