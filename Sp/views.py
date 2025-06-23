from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *

# Create your views here.

def homepage(request):
    return render(request,"Sp/Homepage.html")


def my_pro(request):
    data=tbl_sp.objects.get(id=request.session["sid"])
    return render(request,"Sp/Myprofile.html",{'data':data})

def editprofile(request):
    prodata=tbl_sp.objects.get(id=request.session["sid"])
    if request.method=="POST":
        prodata.sp_name=request.POST.get('txtname')
        prodata.sp_contact=request.POST.get('txtcon')
        prodata.sp_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"Sp/Editprofile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"Sp/Editprofile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_sp.objects.filter(id=request.session["uid"],sp_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                spdata=tbl_sp.objects.get(id=request.session["uid"],sp_password=request.POST.get('txtcurpass'))
                spdata.sp_password=request.POST.get('txtnewpass')
                spdata.save()
                return render(request,"Sp/Changepassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"Sp/Changepassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"Sp/Changepassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"sp/Changepassword.html")

def Myworks(request):
    data=tbl_sp.objects.get(id=request.session["sid"])
    data=tbl_assignorder.objects.filter(sp=request.session["sid"])
    if request.method=="POST":
        data=tbl_assignorder.objects.filter()
        return render(request,"Sp/Myworks.html",{'data':data})
    else:
        return render(request,"Sp/Myworks.html",{'data':data})


def Installstatus(request,aid):
    user = tbl_assignorder.objects.get(id=aid)
    user.assign_status = 1
    user.save()
    return redirect("Sp:homepage")


def MyCRworks(request):
    data=tbl_sp.objects.get(id=request.session["sid"])
    data=tbl_crassignorder.objects.filter(sp=request.session["sid"])
    if request.method=="POST":
        data=tbl_crassignorder.objects.filter()
        return render(request,"Sp/MyCRworks.html",{'data':data})
    else:
        return render(request,"Sp/MyCRworks.html",{'data':data})

def CRInstallstatus(request,aid):
    user = tbl_crassignorder.objects.get(id=aid)
    user.crassign_status = 1
    user.save()
    return redirect("Sp:homepage")