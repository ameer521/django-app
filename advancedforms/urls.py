from django.urls import path

from .views import *

urlpatterns = [

    path('',formbasics,name="formbasics"),
    path('rendering/',renderingform,name="renderingform"),
    path('fields/',formfields,name="formfields"),
    path('viahtml/',collect_via_html,name="collectviahtml"),
    path('viadjango/',collect_via_django_form,name="collectviadjango"),
    path('initial/',inital_or_default_value_setting,name="defaultvaluesetting"),
    path('widget/',widgets_example,name="widgetexample"),
    path('modelform/',Model_Form,name="ModelForm"),




]