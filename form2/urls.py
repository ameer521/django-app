from django.urls import path
from .views import *


####################### FOR CLASSBASED VIEW  ###############################

from django.views.generic.base import  TemplateView

from .views import CustomTemplateView # the class CustomTemplateView from views.py imported

# Here, we imported TemplateView for template fetching.
# The classBased View actually means, There is no need to call a function from view.py file. We can directly call the template in Urls.py.
# for this we imported above TemplateView




urlpatterns = [
    #path('',classview,name="classview"),


    path('',TemplateView.as_view(template_name='form1/homepage.html'),name="classview"),  # Here, We directly called the template by specifying the template name.(look code and understands).



    path('customtemplateview/',CustomTemplateView.as_view(),name="customtemplateview"), #Here,The template fetched by calling class and the "as_view " specifies to load it.

]
