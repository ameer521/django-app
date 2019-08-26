from django.db import models



# Create your models here.


class Sample(models.Model):

    n = models.CharField(max_length=20,null=True,verbose_name="Name")
    age = models.IntegerField(default=18)

    def __str__(self):
        return self.n

