from django.db import models

# Create your models here.

class Ourprojects(models.Model):

    ourprojects_projectname = models.CharField(max_length=100)
    ourprojects_projectdesc = models.TextField()
    ourprojects_projectprice = models.IntegerField()
    ourprojects_review = models.IntegerField()
    ourprojects_projectimg = models.ImageField(upload_to='pics')


class About(models.Model):

    teammembername = models.CharField(max_length=100)
    memberexpertise = models.CharField(max_length=200)
    memberdesc  = models.TextField()
    memberimg = models.ImageField(upload_to='pics')
    memberfacebook = models.CharField(max_length=100)
    membertwitter = models.CharField(max_length=100)
    memberlinkedin = models.CharField(max_length=100)
    membergithub = models.CharField(max_length=100)