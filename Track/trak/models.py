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
    minlvl = models.PositiveIntegerField()
    maxlvl = models.PositiveIntegerField()
    # image = models.ImageField(upload_to='image')
    nowExp = models.ForeignKey(NowExp, on_delete=models.PROTECT)

def __str__(self):
    return self.nameL


class Persons(models.Model):
    nameL = models.TextField()
    minlvl= models.PositiveIntegerField()
    maxlvl = models.PositiveIntegerField()
    image = models.ImageField(upload_to='image')

