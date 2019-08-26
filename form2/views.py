from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Sample

'''
def classview(request):
    return render(request,'form1/homepage.html')'''


################################# CUSTOMOSIZE TEMPLATE VIEW #############################

from django.views.generic.base import TemplateView




class CustomTemplateView(TemplateView):  # here, class created which inherits TemplateView
    template_name = "form1/homepage.html"  # sets the template fetch


# Now we are going to pass context to template (values).

    def get_context_data(self, **kwargs):  # for this we use inbuilt function

        context = super(CustomTemplateView,self).get_context_data(**kwargs) # Here, we called the  " get_context_data " inside the " get_context_data " by calling super() keyword(look and understands)

        names = Sample.objects.all()  # Here, we fetched all objects of model sample
        context["name"] = names   # Then , passed to HTML as "name"

        return context


