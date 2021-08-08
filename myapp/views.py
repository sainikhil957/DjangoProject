from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse, request

from .forms import fdsignupform
from .models import Fdsignup
from .forms import cusignupform
from .models import Cusignup
from .models import Fdform
from .models import Cuitems
from django.db.models import Q

from django.core.mail import EmailMessage
from django.conf import settings

from django.core.files.storage import FileSystemStorage

import os
from django.core.files import File


def index(request):
    return render(request,"index.html")

def sample(request):
    return render(request,"sample.html")

def fdpage(request):
    return render(request,"fdpage.html")

def fdsignup(request):
    return render(request,"fdsignup.html")

def fdregister(request):
    if request.method=="POST":
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        phoneno=request.POST['phoneno']
        email=request.POST['email']
        experience=request.POST['experience']
        designation=request.POST['designation']
        username=request.POST['uname']
        password=request.POST['password']
        data=Fdsignup(firstname=firstname,lastname=lastname,phoneno=phoneno,email=email,experience=experience,designation=designation,username=username,password=password)
        data.save()
        subject="Thank you for registered"
        email=EmailMessage(subject,"You have Successully registered as designer in Fashion Designer Website",to=[email])  #to will take list of email IDs
        email.send()
        return render(request, "fdsignupsuccess.html")
    else:
        return render(request, "fdsignup.html")

def fdsignin(request):
    return render(request,"fdsignin.html")

keyfdsignupid=None
def checkfdsignin(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        flag=Fdsignup.objects.filter(Q(email__iexact=email) & Q(password__iexact=password))
        
        if flag:
            id=Fdsignup.objects.filter(Q(email__iexact=email) & Q(password__iexact=password)).values('id')[0]['id']
            global keyfdsignupid
            def keyfdsignupid():
                return id
            return redirect("fdhome")
        else:
            return render(request,"signupfail.html")
    else:
        return render(request,"fdsignin.html")

def fdhome(request):
    id=keyfdsignupid()
    result=Fdsignup.objects.filter(id=id)
    return render(request,"fdhome.html",{"result":result})

def fdform(request):
    return render(request,"fdform.html")

def fdformstore(request):
    if request.method=="POST" and request.FILES['clothfile']:
        clothname=request.POST['clothname']
        clothfile = request.FILES['clothfile']
        print(clothfile)
        #fs = FileSystemStorage()
        #filename = fs.save(clothfile.name, clothfile)
        clothgender=request.POST['clothgender']
        clothtype=request.POST['clothtype']
        clothcolour=request.POST['clothcolour']
        clothpattern=request.POST['clothpattern']
        clothsizes=request.POST['clothsizes']
        clothprice=request.POST['clothprice']
        id=keyfdsignupid()
        email=Fdsignup.objects.filter(id=id).values('email')[0]['email']
        username=Fdsignup.objects.filter(id=id).values('username')[0]['username']
        data=Fdform(email=email,
                    username=username,
                    clothname=clothname,
                    clothfile=clothfile,
                    clothgender=clothgender,
                    clothtype=clothtype,
                    clothcolour=clothcolour,
                    clothpattern=clothpattern,
                    clothsizes=clothsizes,
                    clothprice=clothprice)
        data.save()
        return render(request,"fdfilesuccess.html")
    else:
        return render(request, "fdform.html")

def fdfiles(request):
    fdsignupid=keyfdsignupid()
    email=Fdsignup.objects.filter(id=fdsignupid).values('email')[0]['email']
    result=Fdform.objects.filter(email=email)
    return render(request, "fdfiles.html",{"result":result,'media_url':settings.MEDIA_URL})

def fdfileview(request,id):
    result=Fdform.objects.filter(id=id)
    return render(request,"fdfileview.html",{"result":result,'media_url':settings.MEDIA_URL})

def fdfiledelete(request,id):
    Fdform.objects.filter(id=id).delete()
    return redirect(fdfiles)


     #CUSTOMER MODULE


def cupage(request):
    return render(request,"cupage.html")

def cusignup(request):
    return render(request,"cusignup.html")

def curegister(request):
    if request.method=="POST":
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        dateofbirth=request.POST['dateofbirth']
        phoneno=request.POST['phoneno']
        email=request.POST['email']
        address=request.POST['address']
        username=request.POST['uname']
        password=request.POST['password']
        data=Cusignup(firstname=firstname,lastname=lastname,dateofbirth=dateofbirth,phoneno=phoneno,email=email,address=address,username=username,password=password)
        data.save()
        subject="Thank you dear customer for registered"
        email=EmailMessage(subject,"You have Successully registered as customer in Fashion Designer Website",to=[email])  #to will take list of email IDs
        email.send()
        return render(request, "cusignupsuccess.html")
    else:
        return render(request, "cusignup.html")

def cusignin(request):
    return render(request,"cusignin.html")

keycusignupid=None
def checkcusignin(request): 
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        flag=Cusignup.objects.filter(Q(email__iexact=email) & Q(password__iexact=password))
        
        if flag:
            cusignupid=Cusignup.objects.filter(Q(email__iexact=email) & Q(password__iexact=password)).values('id')[0]['id']
            global keycusignupid
            def keycusignupid():
                return cusignupid
            return redirect(cuhome)
        else:
            return render(request,"signupfail.html")
    else:
        return render(request,"cusignin.html")

def cuhome(request):
    id=keycusignupid()
    result=Cusignup.objects.filter(id=id)
    return render(request,"cuhome.html",{"result":result})
    

def cuform(request):
    return render(request,"cuform.html")

keycuitemid=None
def cuformcheck(request):
    if request.method=="POST":
        clothgender=request.POST['clothgender']
        clothtype=request.POST['clothtype']
        clothcolour=request.POST['clothcolour']
        clothpattern=request.POST['clothpattern']
        clothsizes=request.POST['clothsizes']
        result=Fdform.objects.filter(clothtype=clothtype,clothcolour=clothcolour,clothpattern=clothpattern,clothsizes=clothsizes,clothgender=clothgender)
        cuitemid= Fdform.objects.filter(clothtype=clothtype,clothcolour=clothcolour,clothpattern=clothpattern,clothsizes=clothsizes,clothgender=clothgender).values('id')[0]['id']
        global keycuitemid
        def keycuitemid():
            return cuitemid
        return render(request,'curesult.html',{"result":result,'media_url':settings.MEDIA_URL})
    else:
        return render(request,'cuform.html')

def cusaveitems(request):
    id=keycuitemid()
    cusignupid=keycusignupid()
    clothname= Fdform.objects.filter(id=id).values('clothname')[0]['clothname']
    clothfile= Fdform.objects.filter(id=id).values('clothfile')[0]['clothfile']
    clothgender= Fdform.objects.filter(id=id).values('clothgender')[0]['clothgender']
    clothtype= Fdform.objects.filter(id=id).values('clothtype')[0]['clothtype']
    clothcolour= Fdform.objects.filter(id=id).values('clothcolour')[0]['clothcolour']
    clothpattern= Fdform.objects.filter(id=id).values('clothpattern')[0]['clothpattern']
    clothsizes= Fdform.objects.filter(id=id).values('clothsizes')[0]['clothsizes']
    clothprice= Fdform.objects.filter(id=id).values('clothprice')[0]['clothprice']
    clothdesigner= Fdform.objects.filter(id=id).values('username')[0]['username']
    username=Cusignup.objects.filter(id=cusignupid).values('username')[0]['username']
    email=Cusignup.objects.filter(id=cusignupid).values('email')[0]['email']

    flag=Cuitems.objects.filter(clothname=clothname,email=email)
    if flag:
        Cuitems.objects.filter(clothname=clothname,email=email).update(cart="1")
        return redirect(cushoppinglist)
    else:
        data=Cuitems(clothdesigner=clothdesigner,clothname=clothname,clothfile=clothfile,clothgender=clothgender,clothtype=clothtype,clothcolour=clothcolour,clothpattern=clothpattern,clothsizes=clothsizes,clothprice=clothprice,username=username,email=email,cart="1")
        data.save()
        return redirect(cushoppinglist)

def cushoppinglist(request):
    cusignupid=keycusignupid()
    email=Cusignup.objects.filter(id=cusignupid).values('email')[0]['email']
    result=Cuitems.objects.filter(email=email,cart="1")
    count=Cuitems.objects.filter(email=email,cart="1").count()
    tp=0
    for i in range(0, count):
        tp=tp+Cuitems.objects.filter(email=email,cart="1").values('clothprice')[i]['clothprice']
    return render(request, "cushoppinglist.html",{"result":result,"tp":tp,'media_url':settings.MEDIA_URL})

def cudeleteitem(request,id):
    Cuitems.objects.filter(id=id).update(cart="0")
    return redirect(cushoppinglist)

def cuviewitem(request,id):
    result=Cuitems.objects.filter(id=id)
    return render(request,"cuviewitem.html",{"result":result,'media_url':settings.MEDIA_URL})

def cusavewishlist(request):
    id=keycuitemid()
    cusignupid=keycusignupid()
    clothname= Fdform.objects.filter(id=id).values('clothname')[0]['clothname']
    clothfile= Fdform.objects.filter(id=id).values('clothfile')[0]['clothfile']
    clothgender= Fdform.objects.filter(id=id).values('clothgender')[0]['clothgender']
    clothtype= Fdform.objects.filter(id=id).values('clothtype')[0]['clothtype']
    clothcolour= Fdform.objects.filter(id=id).values('clothcolour')[0]['clothcolour']
    clothpattern= Fdform.objects.filter(id=id).values('clothpattern')[0]['clothpattern']
    clothsizes= Fdform.objects.filter(id=id).values('clothsizes')[0]['clothsizes']
    clothprice= Fdform.objects.filter(id=id).values('clothprice')[0]['clothprice']
    clothdesigner= Fdform.objects.filter(id=id).values('username')[0]['username']
    username=Cusignup.objects.filter(id=cusignupid).values('username')[0]['username']
    email=Cusignup.objects.filter(id=cusignupid).values('email')[0]['email']
    flag=Cuitems.objects.filter(clothname=clothname,email=email)
    if flag:
        Cuitems.objects.filter(clothname=clothname,email=email).update(wishlist="1")
        return redirect(cushoppinglist)
    else:
        data=Cuitems(clothdesigner=clothdesigner,clothname=clothname,clothfile=clothfile,clothgender=clothgender,clothtype=clothtype,clothcolour=clothcolour,clothpattern=clothpattern,clothsizes=clothsizes,clothprice=clothprice,username=username,email=email,wishlist="1")
        data.save()
        return redirect(cuwishlist)

def cuwishlist(request):
    cusignupid=keycusignupid()
    email=Cusignup.objects.filter(id=cusignupid).values('email')[0]['email']
    result=Cuitems.objects.filter(email=email,wishlist="1")
    return render(request, "cuwishlist.html",{"result":result,'media_url':settings.MEDIA_URL})

def cuwishlistdeleteitem(request,id):
    Cuitems.objects.filter(id=id).update(wishlist="0")
    return redirect(cuwishlist)

def cuwishlisttocart(request,id):
    Cuitems.objects.filter(id=id).update(cart="1")
    return redirect(cushoppinglist)

def paymentmodule(request):
    cusignupid=keycusignupid()
    email=Cusignup.objects.filter(id=cusignupid).values('email')[0]['email']
    count=Cuitems.objects.filter(email=email,cart="1").count()
    tp=0
    for i in range(0, count):
        tp=tp+Cuitems.objects.filter(email=email,cart="1").values('clothprice')[i]['clothprice']
        clothname= Cuitems.objects.filter(cart="1",email=email).values('clothname')[i]['clothname']
        Cuitems.objects.filter(clothname=clothname,email=email).update(order="1")
    result=Cuitems.objects.filter(email=email,cart="1")
    return render(request, "paymentmodule.html",{"result":result,"tp":tp,'media_url':settings.MEDIA_URL})
    
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY 
        return context
def charge(request):
    return render(request,"charge.html")

def codpage(request):
    return render(request,"codpage.html")

def codsuccess(request):
    return render(request,"cashondeliverysuccess.html")

def cuorders(request):
    cusignupid=keycusignupid()
    email=Cusignup.objects.filter(id=cusignupid).values('email')[0]['email']
    result=Cuitems.objects.filter(email=email,order="1")
    count=Cuitems.objects.filter(email=email,order="1").count()
    tp=0
    for i in range(0, count):
        tp=tp+Cuitems.objects.filter(email=email,order="1").values('clothprice')[i]['clothprice']
    return render(request, "cuorders.html",{"result":result,"tp":tp,'media_url':settings.MEDIA_URL})




def gallery(request):
    img = Fdform.objects.filter(clothtype='silk')
    return render(request,'gallery.html',{"img":img, 'media_url':settings.MEDIA_URL})











