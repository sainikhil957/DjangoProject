from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.index,name="index"),
    path('sample/',views.sample,name="sample"),
    path('gallery/',views.gallery,name="gallery"),
    
    path('index/',views.index,name="index"),

    path('fdpage/',views.fdpage,name="fdpage"),
    path('fdsignup/',views.fdsignup,name="fdsignup"),
    path('fdregister/',views.fdregister,name="fdregister"),
    path('fdsignin/',views.fdsignin,name="fdsignin"),
    path('checkfdsignin/',views.checkfdsignin,name="checkfdsignin"),
    path('fdform/',views.fdform,name="fdform"),
    path('fdformstore/',views.fdformstore,name="fdformstore"),
    path('fdfiles/',views.fdfiles,name="fdfiles"),
    path('fdfiledelete/<int:id>',views.fdfiledelete,name="fdfiledelete"),
    path('fdfileview/<int:id>',views.fdfileview,name="fdfileview"),

    path('cupage/',views.cupage,name="cupage"),
    path('cusignup/',views.cusignup,name="cusignup"),
    path('curegister/',views.curegister,name="curegister"),
    path('cusignin/',views.cusignin,name="cusignin"),
    path('checkcusignin/',views.checkcusignin,name="checkcusignin"),
    path('cuform/',views.cuform,name="cuform"),
    path('cuformcheck/',views.cuformcheck,name="cuformcheck"),
    path('cusaveitems/',views.cusaveitems,name="cusaveitems"),
    path('cushoppinglist/',views.cushoppinglist,name="cushoppinglist"),
    path('cudeleteitem/<int:id>',views.cudeleteitem,name="cudeleteitem"),
    path('cuviewitem/<int:id>',views.cuviewitem,name="cuviewitem"),
    
    path('paymentmodule/',views.paymentmodule,name="paymentmodule"),
    path('cuhome/',views.cuhome,name="cuhome"),
    path('fdhome/',views.fdhome,name="fdhome"),
    path('cusavewishlist',views.cusavewishlist,name="cusavewishlist"),
    path('cuwishlist',views.cuwishlist,name="cuwishlist"),
    path('cuwishlistdeleteitem/<int:id>',views.cuwishlistdeleteitem,name="cuwishlistdeleteitem"),
    path('cuwishlisttocart/<int:id>',views.cuwishlisttocart,name="cuwishlisttocart"),
    path('cuorders',views.cuorders,name="cuorders"),

    path('charge',views.charge,name="charge"),
    path('codpage',views.codpage,name="codpage"),
    path('codsuccess',views.codsuccess,name="codsuccess"),

]