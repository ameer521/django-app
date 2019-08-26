from django.contrib import admin

from . import models
from form1.models import Post
from form1.models import TestModel,AbcModelGet
# Register your models here.


class TestModelAdmin(admin.ModelAdmin):  # this class is created for showing an example for timestamp, Here, we specified the fields to show in admin page. We can specify the models to show in admin page by doing this
    fields = [
        'active',
        'title',
        'content',
        'publish',
        'author_email',
        'email',
        'slug',
        'cdate',
        'cdt',
        'udt',
        'tstamp',

        'new_content',
        "get_age",
        "instance_example",


    ]

    readonly_fields = ["udt","tstamp","new_content","get_age","instance_example"]  # Here, we declared the read only fields as " readonly_fields" , so , now it will show in admin page. This is the synatx for it.

    def new_content(self,obj,*args,**kwargs):  # the "new_content" created for an example for creating read only fields , Then we passed "obj"
        #print(obj)
        return str(obj.title)  # then title returned
    # we also declared the function name in readonly_fields and in fields also

    def get_age(self,obj,*args,**kwargs):
        return str(obj.age())

    def instance_example(self,obj,*args,**kwargs):
        return str(obj.age_example)   # if we gives "@property", we dont need to call it as age_example(), just call it as age_example.it just as fields now(look above for fields)

    class Meta: # meta class created , so it will affect for all
        model = TestModel

admin.site.register(Post)
admin.site.register(TestModel, TestModelAdmin)    #Here, We registed "TestModelAdmin" along with "TestModel" for working it. for showing timestamp example.
admin.site.register(AbcModelGet)
