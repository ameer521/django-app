from django.contrib import admin
from .models import *


# Register your models here.


admin.site.register(Foreignkeys)
admin.site.register(ManyToMany)
admin.site.register(OneToOne)
admin.site.register(FromOtherModel)
admin.site.register(ForOnDelete)