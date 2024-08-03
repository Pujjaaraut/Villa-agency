from django.contrib import admin
from .models import Contact
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    cnlist=['cnname','cncontact','cnemail','cnsub','cnmsg']
admin.site.register(Contact, ContactAdmin)