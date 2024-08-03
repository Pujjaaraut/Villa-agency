from django.db import models

# Create your models here.
class Contact(models.Model):
    cnname = models.CharField(max_length=50)
    cncontact = models.IntegerField()
    cnemail = models.CharField(max_length=50)
    cnsub = models.CharField(max_length=50)
    cnmsg= models.CharField(max_length=50)
    def str(self):
        return self.cnname;