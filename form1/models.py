from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.encoding import smart_text
from .validators import validate_email
from django.utils.text import slugify   # the slugify is used to slug the text,. means, if we typed  a word " the laptop" , the space will changed to " - " and the word become " the-laptop".
from datetime import timedelta,datetime,date
from django.db.models.signals import pre_save,post_save    # here, we imported signals
from django.utils.timesince import timesince   # the timesince means the time from since (think about it)




# Create your models here.




class Post(models.Model):
    username = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=25)
    author = models.TextField(max_length=25)

    def __str__(self):
        return smart_text(self.title)





###############################################################################################






#################### FOR WORKING WITH QUERYSETS/ TO OVERRIDE (SEE BELOW QUERYSETS PART) #######################

# Here , we are going to writer two conditions.

# For working TestModel.other.all()
class TestModelMananger(models.Manager): # Here, a classs created to work with querysets,which inherits "Manager"
    def all(self,*args, **kwargs):   # function all() Created
        qs = super(TestModelMananger,self).all(*args,**kwargs).filter(active=True)  # Study the codes, Here, objects filtered with a field "active"
        print(qs)
        return qs

################################################################


class TestModelManager2(models.Manager): # Same like built-in for working TestModel.objects.all()
    def get_queryset(self):
        return TestModelQuerySet(self.model, using=self._db)


    def all(self,*args,**kwargs):
        qs = super(TestModelManager2,self).all(*args,**kwargs)
        print(qs)
        return qs


############################################################################################################






###################################FOR CUSTOM QUERYSETS #######################################################333


class TestModelQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)













################################################### MODELS TUTORIAL  #################################################

##################


CHOICES = [
    ('foot','Football'),
    ('cri','Cricket'),
    ('bas','Basketball')
]
# Here, we created a list of tuples of choices. it is a special syntax for choices. Here , the Choice is displayed as second word " Football " and it will stores in database as "foot"



class TestModel(models.Model):    # always start the model " class " name with Capital letter.Instead of calling "models.model", we can directly call " Model" by importing django.db.models import Model.

    #id = models.BigAutoField(auto_created =True)  # The  " BigAutoField "  is for large numbers
    #id = models.AutoField(auto_created=True)  # here, when the models migrate , this works in " migrations " directory and " ID " creates automaticallly. So we don't need to do it here. The  " autofield " increments value by 1 automatically.
    active = models.BooleanField(default=False)  # in " BooleanField " we need to set a default value or need to set null = True as argument . otherwise , it will ask to create it

    title = models.CharField(max_length=20,default="hello",verbose_name="Post model",unique=True)  # The " CharField" is used for characters. We need to specify the " max_length" ,and the " default" . otherwise set the "null=True".If we didnt do this, it will not migrate.The "verbose_name" is used to show the content inside it instead of the variable name. Here, instead of showing " title ", it will show " Post model ".

    content = models.TextField(null=True, blank=True) #" TextField " is for large field. We dont want to set max length here, but need to set default. otherwise set "null = True".the "blank=True" also allows it to blank.



#################### CHOICE #######################################


    publish = models.CharField(null=True,max_length=30,choices=CHOICES,default='foot') # here, we assigned  "CHOICES " for choices variable. Thus , it will get the choices inside it. We also set the default value here as "foot", so we can see Football as default.


############### FOR OVERRIDING objects.all() to other.all() #########


    other = TestModelMananger()   # inorder to work TestModel.other,.all() , we need to register it with the modelmanager in the class we are going to use
    objects = TestModelManager2() # objects also registered , so , TestModel.objects,all() still works, but with condition inside the TestModelManager2 (Which is written as bulit-in)




##################### CUSTOM VALIDATION #########################


    author_email = models.CharField(max_length = 50,verbose_name ='email',unique=True,validators=[validate_email],null=True)  # here, the custom validators used.

###########################################################################################


#############################DJANGO'S BUILTIN EMAIL FIELD #####################################
    email = models.EmailField(null=True,verbose_name="Django Bulitin email")   # if we use django's built in emailfield, the field must not be empty even if we set "null = True " and it must validates email format which checks " @ " , " .com" exist or not in a proper way.


# here, we created an email field, for validators , we imported ValidationError from core.Exceptions. Then , we created a function for validation above.
    # The "validators" are given as list and it is it's syntax. Then , we moved the above function to a file named validators for easy use and imported the functions to models.

######################################################################################################################

########################### SLUG FIELD ##########################

    slug = models.SlugField(null= True,blank=True)  #the text cannot be written with space ( means, if we typed " The laptop" it is not allowed, we need to type  as " the-laptop" ). space is not allowed between words or values

################################################################



####################DATE FIELD ###########################

    cdate = models.DateField(verbose_name="DateField",default=timezone.now)


#######################################################################







#################### TIMESTAMP & DATE TIME FIELD ########################


    cdt = models.DateTimeField(verbose_name="CreatedDate",default=timezone.now)
    udt = models.DateTimeField(verbose_name="Updated ",auto_now=True)
    tstamp = models.DateTimeField(verbose_name="Timestamp",auto_now_add= True)

# the timestamp means when that model created. Here, tstamp, so ,we uses "auto_now_add" for this.
# if we only declared "auto_now" , then it shows , when it last saved.
# we can't see these in admin page normally

############################# TIME SINCE ########################

    #ts = timesince(cdt)


#################################################################




##########################FOR SHOWING CUSTOM ERROR MESSAGE #####################

    eshow = models.CharField(null=True,
                             max_length=30,
                             unique=True,
                             verbose_name="For Custom Error show",
                             error_messages={
                                 "unique":" This field Must not be repeated",
                                 "required":"Value required ",
                             },
                             help_text="This field should not be null and must be unique"
                             )

# Here,  we gives our own error messages for each particular conditions such as unique , required. we can give error messages in dictionary , so , if the unique condition not satisfies, it wil show custom error messages instead of django bulit in message . but , only unique will works now and rest of them such as required is in development stage , so it will not work.
# we can also give help text in "help_text" , so it will be shown as help text .
##################################################

    class Meta:   # if we sets  verbose in meta , it will show content inside it as model name .
        verbose_name = 'PostTest'
        verbose_name_plural = 'posting' # the verbose plural is same like verbose name , but it will show instead of verbose name in admin page,(look and run code).refer meaning of plural for understanding.



############################ UNICODE OR DISPLAYING  CONTENT INSTEAD OF OBJECT IN ADMIN ################


    def __str__(self):
        return smart_text(self.title)  #it will dispaly content may be in other languages too , need to import library smart_text from utils,same like below.
        #return self.title# it will display the returned content.(you already knows what it means )


# the " unique is for builtin validation. it will check for uniqueness of values in fields. See " title " variable.


#######################################################################################################





########################### OVERRIDING THE SAVE METHOD (NOT RECOMMENDED IN ALL CASE ####################################

    def save(self,*args,**kwargs):
        # this function is used to over ride the current save function  in admin page. it is not recommended.Here, the values are passed as args and kwargs for error free.
        if not self.slug:  # here, we checked if there is a slug given or not .
            self.slug = slugify(self.title) # if not, the slug field will get the slugified value of title.

        super(TestModel,self).save(*args,**kwargs)# here, the content is saves to testmodel
        print("working")  # for testing , the above save working or not . But ,



############################ INSTANCE METHODS AND PROPERTIES ################################################

# instance methods are methods written inside a class.



    def age(self):  # simple example

        #return timesince(self.cdt) # for getting since time from created date

        return "{}ago".format(timesince(self.cdt) )  # modified with .format



    @property     # if we gives a function as "@property" , it doesn't need to call with " () ",only just need functon name to call. it will change like fields in models like title, date etc
    def age_example(self): # example for instance
        if(self.cdt):
            now = datetime.now()
            print(now)
            publish_time = datetime.combine(
                self.cdt,
                datetime.now().min.time()

            )

            try:
                difference = now - publish_time
            except:
                return "Unknown"

            if (difference <= timedelta(minutes=1)):
                return "just now"
            else:
                return timesince(publish_time)



#############################################################################################################






######################## SIGNALS  ###########################3333

### PRE SAVE #################


# The signals are used to give signals . eg: to show any message before saving or after saving or checking any conditions etc

def testmodel_pre_save(sender,instance,*args,**kwargs):   # here, a function created for pre_save and attributes are syntax for it
    print("before save")

pre_save.connect(testmodel_pre_save,sender=TestModel)      # we need to tell , which function is  " pre_save " by calling imported "pre_save"  and connecting it to that function by pasing as argument. Then we need to pass the model as argument we need to use in  "pre_save " as sender.

def testmodel_post_save(sender,instance,*args,**kwargs):  # function created for post_save. syntax same as " post_save".
    print("After Save")


post_save.connect(testmodel_post_save,sender=TestModel)    # same like " post_save"


##########################################################################################################################




class AbcModelGet(models.Model):  # Here , we created model as "AbcModelGet" . So , in admin page , we can see it as " Abc Model Gets ". When we gives capital letter , it will give space and also adds " s " with last letter.
    title = models.TextField(default='hello')


'''do makemigrations and migrate every time when models created. When this done, a file is created at the directory " migrations " with these content.
when we do this , automatically an ID is created , So we dont need to do it manually and it will increment.

'''

###############################  WORKING WITH QUERY SETS ####################################################
#   python manage.py shell  -> first open shell
#   from form1.models import TestModel    -> Then import the model to be work with , Here, TestModel imported
#   qs = TestModel.objects.all()    -> for fetching all objects , Now , the qs contain all objects details

# The " qs " is actually now a list which contain all objects. So we can loop over it

# for i in qs:
#    print(i.title)   -> Here, the title of each object will be printed.

#    newobj = Testmodel.objects.create(title="Created By shell")   -> Here, We created a newobject. for this we uses "create " and the field "title" is sets.
# We can set other field too by separating fields with commas like below,
#         newobject = TestModel.objects.create(title="Created with shell2",content="With shell")

#    qs.count()  -> to get total objects count

#    filter = TestModel.objects.filter(title="hello")  # The " filter " is used to filter objects by our conditions. Here , the object filtered with title " hello "

#    filter1 = testModel.objects.filter(title__icontains="created")  -> Here, we used "__icontains " with title, So , all objects with title having word " created " will be fetched.



# When we gives TestModel.objects.all() , it will show all objects. But , we can override this condition with our like , for this we do the following,

'''class TestModelMananger(models.Manager):
    def all(self,*args, **kwargs):
        qs = super(TestModelMananger,self).all(*args,**kwargs).filter(active=True)  # The explanation  for this code is given above (look top)
        print(qs)
        return qs '''
