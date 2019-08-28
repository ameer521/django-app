from django import forms
from django.utils import timezone

from .models import Formmodel

class firstform(forms.Form):  # a form created
    q = forms.CharField(max_length=20)   # field declared ,Here, we declared the field as " q " , so it will act a query, so we dont need to give name="q" like we given in HTML page.


class fieldsform(forms.Form):  # for showing  fields
    text_field = forms.CharField(min_length=2,max_length=20,initial="text")    # the initial means default, we can set it here or we can pass it in view(look view for example)
    Integer_field = forms.IntegerField(initial=10)
    boolean_field = forms.BooleanField(initial=False)
    email_field = forms.EmailField(min_length=8)



########  BASIC VALIDATION ############################

# here , These functions are inbuit which will automatically runs during form validation and will validate.

    def clean_Integer_field(self): #These are  inbuit functions
        integer = self.cleaned_data.get("Integer_field")          # here , the value fetched
        if integer < 10:
            raise forms.ValidationError("The Value must be Greater than 10")  # if the condition fails , it will raise ValidationError
        return integer   # otherwise returns the value



    def clean_text_field(self):   # for text field validation, for
        text = self.cleaned_data.get("text_field")
        if len(text) < 6:
            raise forms.ValidationError("The name must be more than 6 characters")
        return text



################# FORM FOR LABEL & WIDGET ################################


CHOICES = [
    ("t1","test1"),
    ("t2","test2"),   # The syntax for choice is same like in model ,

]


YEARS = [ x for x in range(1990,2019) ]   # for custom Date Widget, syntax same like choices, we given it in a list




class forwidget(forms.Form):

    text = forms.CharField(max_length=25,initial="WidgetTextexample",widget=forms.Textarea())  # here, the widget created, now the charfield changes to textarea . means it's area increased.

    text_by_cols_rows = forms.CharField(max_length=25,widget=forms.Textarea(attrs={"rows":2,"cols":4})) # we can define the size of the widget area by specifying row and column as attributes


    label_example = forms.CharField(min_length=25,label="Label") # here, the Label name given , so the label name will be shown instead of variable name.

    choices = forms.CharField(label="Choices",widget=forms.Select(choices=CHOICES)) # Here, we used " Select " Widget, So we used "chioces"  here,

    ckbox = forms.CharField(label="CheckBox",widget=forms.CheckboxSelectMultiple(choices=CHOICES))  # for multiple  checkbox select


    typechoice = forms.TypedChoiceField(label="Type Choice",choices=CHOICES)  # for choice field,instead of specifying in widget we can directly use choice field

    radiobox = forms.CharField(label="RadioBox",widget=forms.RadioSelect(choices=CHOICES))  # for radio box

    datefield = forms.DateField(label="DateField",widget=forms.SelectDateWidget())  # for datefield, The widget helps to select date instead of typing

    customdaterange = forms.DateField(label="CustomDateRange",widget=forms.SelectDateWidget(years=YEARS)) # for custom Year selection








#####################################################################################################






################### MODEL FORM #############################################################

# for working model form , we need to import the model we want from model.py

# so ,we imported the FormModel above


# The use of modelForm is that, we dont need to create fields in Form.py, we can inherit all fields from model.py


class FormModelform(forms.ModelForm):    #imported The ModelForm

    class Meta:
        model = Formmodel  # model selected
        fields = ["n","age","address","stat","file"]   # we selected the field to show in form


        #exclude= ["post"]  # if we uses exclude , all other fields except fields in the exclude will be shown in form.


# we can validate here in modelForm too

    def clean_n(self):
        text = self.cleaned_data.get("n")
        if len(text) < 6:
            raise forms.ValidationError("The name should be more than 6 letters")
        return text




######################### OVER RIDING SAVE METHOD OF MODEL FORM ###############################

 #   def save(self,commit=True,*args,**kwargs):
  #      obj =super(Formmodel, self).save(commit=False,*args,**kwargs)  # now ,we set commit as False, so the it will not save before we save

#        obj.content = "Coming Soon"    # so , we can include our own fields before save
 #       if commit:    #
  #          obj.save() # when ,commit, it will save
   #     return obj



###################################FORM FOR CUSTOM ERROR MESSASGES #####################################

class Customerrrormessage(forms.ModelForm):

    class Meta:
        model = Formmodel
        fields = ["n","age","address"]

        labels={
            "n":"Name Field",   # we can change label name of field here too
            "age":"Age field",
        }

        help_texts = {
            "n": "For name",     # we can set help text here
            "age":"For Age",
        }

        error_messages = {
            "n" : {
                "required":"Please Enter the Name",
                "unique":"Name already exist"},                    # here, error message for each field given,look structure


            "age":{
                "required":"please enter the age",
            }
        }