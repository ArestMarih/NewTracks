from django.db import models

class quest(models.Model):
    nameQu = models.CharField(max_length=128)
    comments = models.TextField(null=True,blank=True)
    exp = models.PositiveIntegerField(default=0)
    done = models.BooleanField(default=False)

class NowExp(models.Model):
    expe = models.PositiveIntegerField(default=0)
    Total_money = models.BigIntegerField(default=0)

def __str__(self):
    return self.nameL

class Persons(models.Model):
    nameL = models.TextField()
    minlvl= models.PositiveIntegerField()
    maxlvl = models.PositiveIntegerField()
    image = models.ImageField(upload_to='image')

class CatFin(models.Model):
    Cat = models.TextField()

class Finance(models.Model):
    name_f = models.TextField()
    desc = models.TextField()
    Income = models.BooleanField(default=None)
    count = models.BigIntegerField(default=0)
    category = models.ForeignKey(CatFin, on_delete=models.PROTECT)

