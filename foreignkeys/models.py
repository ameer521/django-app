from django.db import models
from django.conf import settings
from django.utils.encoding import smart_text

# Create your models here.

User = settings.AUTH_USER_MODEL      # here, we gives the User path for use as foreign key

class Foreignkeys(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    n = models.CharField(max_length=25,null=True,verbose_name="name")



    def __str__(self):
        return self.n


############################ MANY TO MANY FILED ############################3

class ManyToMany(models.Model):

    user = models.ManyToManyField(User)     # the manytomany filed means, many user can be the owner of one car and a sigle user can be the owner of different cars

    car = models.CharField(max_length=25,null=True)


    def __str__(self):
        return smart_text(self.car)





########################### ONE TO ONE FIELD ##################################



class OneToOne(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)     # this field means, it can have only one value. Means , a user can only have a car , not more than one .if we  tried , the user exist with a value will displays .

    car = models.CharField(max_length=25,null=True)





    def __str__(self):
        return smart_text(self.car)




############################## FOREIGN KEY FROM OTHER MODEL  ########################################




class FromOtherModel(models.Model):

    user = models.ForeignKey(OneToOne,on_delete=models.CASCADE)    # here, we used value of " Onetoone " class as foreign key.






################################# DIFFERENT DELETE INSTANCES / ON_DELETE #########################


class ForOnDelete(models.Model):

    user1 = models.ForeignKey(User,verbose_name="CASCADE",on_delete=models.CASCADE)

    user3 = models.ForeignKey(User, verbose_name="SET NULL", null=True,on_delete=models.SET_NULL)

    user2 = models.ForeignKey(User, verbose_name="DEFAULT", on_delete=models.SET_DEFAULT, default="admin")




























####################### RELATION IN  SHELL ##################################

# obj = Foreignkeys.objects.first()   -> to fetch first object
# user = obj.user   -> for fetching user
# print(user.password)  -> for password of user
# print(user.email)       -> for email of user
# user.__class__   => to find the user belongs to which class



########################## CHANGING OWNERSHIP ###############################

# obj = Foreignkeys.objects.first()   -> to fetch first object
# user = obj.user   -> for fetching user

# user = obj.user.__class__    -> for getting user class , then we can change ownership. Here, the class user.model imported

# Users = user.objects.all()    -> to fetch all users

# here, as example, we have user "admin" and "ameer"

# admin = user.objects.first()  -> here, the user admin stored to admin

# ameer = user.objects.last()    -> ameer user stored to ameer

# as example, we have first object user as admin, now , we are going to change it to user "ameer"
# for this,

# obj = foreignkeys.objects.first()

# obj.user  = ameer   -> ,now , the first object user changed from "admin" to " ameer ".

# obj.save()  -> now ,saved ,so change user.










