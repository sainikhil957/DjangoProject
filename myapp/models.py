from django.db import models

# Create your models here.
class Fdsignup(models.Model):
    firstname=models.CharField(max_length=100,blank=False)
    lastname=models.CharField(max_length=100,blank=False)
    phoneno=models.CharField(max_length=100,blank=False)
    email=models.EmailField(max_length=100,blank=False)
    #experience_choices = (('less than 2 years','less than 2 years'),('2 years','2 years'),('4 years','4 years'),('more than 4 years','more than 4 years'))
    #experience=models.CharField(max_length=100,choices=experience_choices,blank=False)
    experience=models.CharField(max_length=100,blank=False)
    #designation_choices = (('retail manager','retail manager'),('textile designer','textile designer'),('sketching assistant','sketching assistant'),('fashion journalist','fashion journalist'))
    #designation=models.CharField(max_length=100,choices=designation_choices,blank=False)
    designation=models.CharField(max_length=100,blank=False)
    username=models.CharField(max_length=100,blank=False)
    password=models.CharField(max_length=100,blank=False)
    class Meta:
        db_table="fdsignup_table"


class Cusignup(models.Model):
    firstname=models.CharField(max_length=100,blank=False)
    lastname=models.CharField(max_length=100,blank=False)
    dateofbirth=models.CharField(max_length=100,blank=False)
    phoneno=models.CharField(max_length=100,blank=False)
    email=models.EmailField(max_length=100,blank=False)
    address=models.CharField(max_length=100,blank=False)
    username=models.CharField(max_length=100,blank=False,default=None)
    password=models.CharField(max_length=100,blank=False)
    class Meta:
        db_table="cusignup_table"


class Fdform(models.Model):
    clothname=models.CharField(max_length=100,blank=False,default=None)
    clothfile=models.ImageField(upload_to='media/image',default='')
    clothgender=models.CharField(max_length=100,blank=False,default=None)
    clothtype=models.CharField(max_length=100,blank=False)
    clothcolour=models.CharField(max_length=100,blank=False)
    clothpattern=models.CharField(max_length=100,blank=False)
    clothsizes=models.CharField(max_length=100,blank=False)
    clothprice=models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True,default=None)
    username=models.CharField(max_length=100,blank=False,default=None)
    email=models.CharField(max_length=100,blank=False,default=None)
    class Meta:
        db_table="fdform_table"

class Cuitems(models.Model):
    clothname=models.CharField(max_length=100,blank=False)
    clothfile=models.ImageField(upload_to='media/image',default='')
    clothgender=models.CharField(max_length=100,blank=False)
    clothtype=models.CharField(max_length=100,blank=False)
    clothcolour=models.CharField(max_length=100,blank=False)
    clothpattern=models.CharField(max_length=100,blank=False)
    clothsizes=models.CharField(max_length=100,blank=False)
    clothprice=models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True,default=None)
    clothdesigner=models.CharField(max_length=100,blank=False,default=None)
    username=models.CharField(max_length=100,blank=False)
    email=models.CharField(max_length=100,blank=False,default=None)
    cart=models.CharField(max_length=100,blank=False,default="0")
    wishlist=models.CharField(max_length=100,blank=False,default="0")
    order=models.CharField(max_length=100,blank=False,default="0")
    class Meta:
        db_table="cuitems_table"
