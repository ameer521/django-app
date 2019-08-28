from django.urls import path

from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('',formbasics,name="formbasics"),
    path('rendering/',renderingform,name="renderingform"),
    path('fields/',formfields,name="formfields"),
    path('viahtml/',collect_via_html,name="collectviahtml"),
    path('viadjango/',collect_via_django_form,name="collectviadjango"),
    path('initial/',inital_or_default_value_setting,name="defaultvaluesetting"),
    path('widget/',widgets_example,name="widgetexample"),
    path('modelform/',Model_Form,name="ModelForm"),
    path('fileupload/',image_upload_via_html,name="fileupload"),
    path('viamodelform/',file_upload_model_form,name='viamodelform'),
    path('adjustdatainview/',adjusting_model_form_data_in_view,name="adjustinginview"),
    path('customerrormessage/',custom_error_messages,name="customerrormessages"),

] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)