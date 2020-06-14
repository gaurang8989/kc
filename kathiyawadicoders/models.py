from django.db import models

# Create your models here.

class Home(models.Model):

    home_projectname = models.CharField(max_length=100)
    home_projectimg = models.ImageField(upload_to='pics')
    home_projectdesc = models.TextField()
    home_projectprice = models.IntegerField()
    home_projectreview = models.IntegerField()