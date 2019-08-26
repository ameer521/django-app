from django.shortcuts import render

from .forms import *

# Create your views here.


########### FOR BASICS ##########################################333

def formbasics(request):

    title = "Advanvced Form Section"
    return render(request,"advancedforms/basics.html",{"title":title})


####################### FOR RENDERING ######################################

def renderingform(request):


    form = firstform()   # here, we fetched firstform and passed to HTML page
    return render(request,"advancedforms/rendering.html",{"form":form})



#################### FOR FORM FIELDS #######################################



def formfields(request):

    form = fieldsform()
    return render(request,'advancedforms/formfields.html',{"form":form})



######################## COLLECT VIA HTML #######################33333333


def collect_via_html(request):  # going to collect data only via HTML form  , we need to set {% csrf_token  %} in HTML for security

    if request.method == "POST":
        print(request.POST.get("searching"))  # here, the typed text in the HTML form retrieved." searching " is the name of the textbox



    return render(request,'advancedforms/collectviahtml.html',{})



######################## COLLECT VIA DJANGO FORM ######################


def collect_via_django_form(request):

    form = fieldsform(request.POST or None)

    if form.is_valid(): # here, we checked if the form is valid or not
        print(form.cleaned_data)  # printed all the data entered in the form
        print(form.cleaned_data.get("text_field")) # to get by field name





    return render(request,"advancedforms/viadjangoform.html",{"form":form})



###############SETTING INITIAL VALUE #####################

# the initial value means default value for forms can be set in the view or in the form

def inital_or_default_value_setting(request):


    form = fieldsform(request.POST or None, initial={"text_field":"hello","Integer_field":20})  # Directly passed the default value by specifying the variable name,

    return render(request,"advancedforms/initial_or_default.html",{"form":form})

# we can also pass initial as follows instead of passing intial value directly as argument

  # default = {"text_field":"hai","Integer_field":30}

  # form = fieldsform(request.POST or None, initial=default)

######################################################################


################################## WIDGETS ########################################

def widgets_example(request):

    form = forwidget(request.POST or None)

    return render(request,'advancedforms/widget.html',{"form":form})






def Model_Form(request):

    form = FormModelform(request.POST or None)

    if form.is_valid():   # here , if the form is valid , then it will saves to database.
        form.save()
        print("Saved")

    return render(request,'advancedforms/modelform.html',{"form":form})


















