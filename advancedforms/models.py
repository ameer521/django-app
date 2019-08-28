from django.db import models


# Create your models here.
class Formmodel(models.Model):
    n = models.CharField(verbose_name="name",null=True,max_length=25)
    age = models.IntegerField(verbose_name="Age",default=18)
    address = models.CharField(max_length=50,null=True,verbose_name="Home Address")
    post = models.TextField(max_length=25,null=True)
    stat = models.BooleanField(default=True,verbose_name="Passed")
    file = models.FileField(upload_to='media',blank=True)


    def __str__(self):
        return self.n


