from django.contrib import admin
from .models import Contact,MyModel,Signup
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    cnlist=['cnname','cncontact','cnemail','cnsub','cnmsg']
admin.site.register(Contact, ContactAdmin)
class MyModelAdmin(admin.ModelAdmin):
    mlist=['name','age']
admin.site.register(MyModel, MyModelAdmin)

class SignupAdmin(admin.ModelAdmin):
    mlist=['name','age']
admin.site.register(Signup, SignupAdmin)
