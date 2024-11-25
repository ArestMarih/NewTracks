from django.db import models

class quest(models.Model):
    nameQu = models.CharField(max_length=128)
    comments = models.TextField(null=True,blank=True)
    exp = models.PositiveIntegerField(default=0)
    done = models.BooleanField(default=False)

class NowExp(models.Model):
    expe = models.PositiveIntegerField(default=0)

class Person(models.Model):
    nameL = models.TextField()
    maxlvl = models.PositiveIntegerField()
    # image = models.ImageField(upload_to='image')
    nowExp = models.ForeignKey(NowExp, on_delete=models.PROTECT)

class Persons(models.Model):
    nameL = models.TextField()
    maxlvl = models.PositiveIntegerField()
    image = models.ImageField(upload_to='image')

class Persona(models.Model):
    name = models.TextField(max_length=20)
    exp = models.PositiveIntegerField()

class Lvls(models.Model):
    title = models.TextField()
    minExp = models.PositiveIntegerField()
    maxExp = models.PositiveIntegerField()
    img = models.ImageField( upload_to=None, blank=True, null=True)
   