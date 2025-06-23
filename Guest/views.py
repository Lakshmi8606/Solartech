from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *


# Create your views here.


def NewuserInsertSelect(request):
    data=tbl_newuser.objects.all()
    district=tbl_district.objects.all()
    place=tbl_place.objects.all()
    if request.method=="POST":
        username=request.POST.get("txtname")
        gender=request.POST.get("gender")
        contact=request.POST.get("txtcontact")
        email=request.POST.get("txt_email")
        password=request.POST.get("txt_password")
        district=tbl_district.objects.get(id=request.POST.get("ddldistrict"))
        place=tbl_place.objects.get(id=request.POST.get("place"))
        tbl_newuser.objects.create(user_name=username,user_gender=gender,user_contact=contact,user_email=email,user_password=password,user_photo=request.FILES.get("fileImage"),user_proof=request.FILES.get("fileProof"),place_name=place)
        return render(request,"Guest/Newuser.html",{'data':data})
    else:
        return render(request,"Guest/Newuser.html",{'data':data,'district':district,'place':place})


def ajaxplace(request):
    dis = tbl_district.objects.get(id=request.GET.get("did"))
    place = tbl_place.objects.filter(district_name=dis)
    return render(request,"GUEST/AjaxPlace.html",{"place":place})


def Login(request):
    if request.method == "POST":
        usercount = tbl_newuser.objects.filter(user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password")).count()
        spcount = tbl_sp.objects.filter(sp_email=request.POST.get("txt_email"),sp_password=request.POST.get("txt_password")).count()
        admincount = tbl_admin.objects.filter(admin_email=request.POST.get("txt_email"),admin_password=request.POST.get("txt_password")).count()
        if usercount > 0:
            user = tbl_newuser.objects.get(user_email=request.POST.get("txt_email"),user_password=request.POST.get("txt_password"))
            request.session["uid"] = user.id
            request.session["uname"] = user.user_name
            return redirect("User:index")
        elif spcount > 0:
            sp = tbl_sp.objects.get(sp_email=request.POST.get("txt_email"),sp_password=request.POST.get("txt_password"))
            request.session["sid"] = sp.id
            request.session["spname"] = sp.sp_name
            return redirect("Sp:homepage")
        elif admincount > 0:
            admin = tbl_admin.objects.get(admin_email=request.POST.get("txt_email"),admin_password=request.POST.get("txt_password"))
            request.session["aid"] = admin.id
            request.session["aname"] = admin.admin_name
            return redirect("WebAdmin:index")
        else:
            return render(request,"Guest/Login.html",{"msg":"Invalid Email Or Password"})
    else:
        return render(request,"Guest/Login.html")






def SpInsertSelect(request):
    data=tbl_sp.objects.all()
    district=tbl_district.objects.all()
    place=tbl_place.objects.all()
    if request.method=="POST":
        spname=request.POST.get("txtname")
        gender=request.POST.get("gender")
        contact=request.POST.get("txtcontact")
        email=request.POST.get("txtemail")
        qualification=request.POST.get("txtqualification")
        password=request.POST.get("txtpassword")
        district=tbl_district.objects.get(id=request.POST.get("ddldistrict"))
        place=tbl_place.objects.get(id=request.POST.get("place"))
        tbl_sp.objects.create(sp_name=spname,sp_gender=gender,sp_contact=contact,sp_qualification=qualification,sp_email=email,sp_password=password,sp_photo=request.FILES.get("fileImage"),sp_proof=request.FILES.get("fileProof"),place_name=place)
        return render(request,"Guest/Spreg.html",{'data':data})
    else:
        return render(request,"Guest/Spreg.html",{'data':data,'district':district,'place':place})


def index(request):
    if request.method == "POST":
        return render(request, "Guest/index.html")
    else:
        return render(request, "Guest/index.html")

