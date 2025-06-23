from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from User.models import *
from datetime import date


# Create your views here.

def DistrictInsertSelect(request):
    data=tbl_district.objects.all()
    if request.method=="POST":
        disname=request.POST.get("txtdist")
        tbl_district.objects.create(district_name=disname)
        return render(request,"Admin/District.html",{'data':data})
    else:
        return render(request,"Admin/District.html",{'data':data})

def delDistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("WebAdmin:DistrictInsertSelect")


def Districtupdate(request,eid):
    editdata=tbl_district.objects.get(id=eid)
    if request.method=="POST":
        editdata.district_name=(request.POST.get("txtdist"))
        editdata.save()
        return redirect("WebAdmin:DistrictInsertSelect")
    else:
        return render(request,"Admin/District.html",{'editdata':editdata})

def PlaceInsertSelect(request):
    data=tbl_place.objects.all()
    district=tbl_district.objects.all()
    if request.method=="POST":
        placename=request.POST.get("txtplace")
        disid=tbl_district.objects.get(id=request.POST.get("ddldistrict"))
        tbl_place.objects.create(place_name=placename,district_name=disid)
        return render(request,"Admin/Place.html",{'data':data})
    else:
        return render(request,"Admin/Place.html",{'data':data,'district':district})

def delPlace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect("WebAdmin:PlaceInsertSelect")


def Placeupdate(request,eid):
    editdata=tbl_place.objects.get(id=eid)
    if request.method=="POST":
        editdata.place_name=(request.POST.get("txtplace"))
        editdata.save()
        return redirect("WebAdmin:PlaceInsertSelect")
    else:
        return render(request,"Admin/Place.html",{'editdata':editdata})



def  CategoryInsertSelect(request):
    data=tbl_category.objects.all()
    if request.method=="POST":
        catname=request.POST.get("txtcat")
        tbl_category.objects.create(category_name=catname)
        return render(request,"Admin/Category.html",{'data':data})
    else:
        return render(request,"Admin/Category.html",{'data':data})

def delcategory(request,did):
    tbl_category.objects.get(id=did).delete()
    return redirect("WebAdmin:CategoryInsertSelect")

def Categoryupdate(request,eid):
    editdata=tbl_category.objects.get(id=eid)
    if request.method=="POST":
        editdata.category_name=(request.POST.get("txtcat"))
        editdata.save()
        return redirect("WebAdmin:CategoryInsertSelect")
    else:
        return render(request,"Admin/Category.html",{'editdata':editdata})


def Adminreg(request):
    data=tbl_admin.objects.all()
    if request.method=="POST":
        adminname=request.POST.get("txtname")
        admincontact=request.POST.get("txtcontact")
        adminemail=request.POST.get("txtemail")
        adminpassword=request.POST.get("txtpass")
        tbl_admin.objects.create(admin_name=adminname,admin_contact=admincontact,admin_email=adminemail,admin_password=adminpassword)
        return render(request,"Admin/Adminreg.html",{'data':data})
    else:
        return render(request,"Admin/Adminreg.html",{'data':data})

def delAdminreg(request,did):
    tbl_admin.objects.get(id=did).delete()
    return redirect("WebAdmin:Adminreg")


def Adminregupdate(request,eid):
    editdata=tbl_admin.objects.get(id=eid)
    if request.method=="POST":
        editdata.admin_name=(request.POST.get("txtname"))
        editdata.admin_contact=(request.POST.get("txtcontact"))
        editdata.admin_email=(request.POST.get("txtemail"))
        editdata.admin_password=(request.POST.get("txtpass"))
        editdata.save()
        return redirect("WebAdmin:Adminreg")
    else:
        return render(request,"Admin/Adminreg.html",{'editdata':editdata})


def UserviewInsertSelect(request):
    data=tbl_newuser.objects.all()
    return render(request,"Admin/Userview.html",{'data':data})
        

def delUserview(request,did):
    tbl_newuser.objects.get(id=did).delete()
    return redirect("WebAdmin:UserviewInsertSelect")


def Userlistview(request):
    userdata = tbl_newuser.objects.filter(user_status=0)
    return render(request,"Admin/Userlistview.html",{"userdata":userdata})

def Useraccept(request,aid):
    user = tbl_newuser.objects.get(id=aid)
    user.user_status = 1
    user.save()
    return redirect("WebAdmin:LoadingHomePage")

def Userreject(request,rid):
    user = tbl_newuser.objects.get(id=rid)
    user.user_status = 2
    user.save()
    return redirect("WebAdmin:LoadingHomePage")

def Useracceptedlist(request):
    userdata = tbl_newuser.objects.filter(user_status=1)
    return render(request,"Admin/Useraccept.html",{"userdata":userdata})

def Userrejectedlist(request):
    userdata = tbl_newuser.objects.filter(user_status=2)
    return render(request,"Admin/Userreject.html",{"userdata":userdata})


def LoadingHomePage(request):
    return render(request,"Admin/Homepage.html")

def subcategRegistration(request):
    category = tbl_category.objects.all()
    data=tbl_subcategory.objects.all()
    if request.method=="POST":
        subcategName=request.POST.get('txtsubcateg')
        cat = tbl_category.objects.get(id=request.POST.get('sel_category'))
        tbl_subcategory.objects.create(subcateg_name=subcategName,category=cat)
        return redirect("WebAdmin:subcategRegistration")
    else:
        return render(request,"Admin/Subcategory.html",{'data':data,'categorydata':category})
    
def delSubcateg(request,did):
    tbl_subcategory.objects.get(id=did).delete()
    return redirect("WebAdmin:subcategRegistration")

def Subcategupdate(request,eid):
    category = tbl_category.objects.all()
    editdata=tbl_subcategory.objects.get(id=eid)
    if request.method=="POST":
        editdata.subcateg_name=request.POST.get("txtsubcateg")
        cat = tbl_subcategory.objects.get(id=request.POST.get('sel_category'))
        editdata.category = cat
        editdata.save()
        return redirect("WebAdmin:subcategRegistration")
    else:
        return render(request,"Admin\Subcategory.html",{"editdata":editdata,"editdata":category})


def ProductInsertSelect(request):
    data=tbl_product.objects.all()
    category=tbl_category.objects.all()
    brand=tbl_brand.objects.all()
    procat=tbl_productcategory.objects.all()
    if request.method=="POST":
        productname=request.POST.get("txtpname")
        productprice=request.POST.get("txtprice")
        productdesc=request.POST.get("txtdesc")
        catid=tbl_category.objects.get(id=request.POST.get("sel_category"))
        brandid=tbl_brand.objects.get(id=request.POST.get("sel_brand"))
        pcid=tbl_productcategory.objects.get(id=request.POST.get("sel_pc"))
        tbl_product.objects.create(product_name=productname,product_price=productprice,product_desc=productdesc,product_image=request.FILES.get("fileImage"),category_name=catid,brand_name=brandid,productcategory_name=pcid)
        return render(request,"Admin/Product.html",{'data':data})
    else:
        return render(request,"Admin/Product.html",{'data':data,'category':category,'brand':brand,'productcategory':procat})










def ajaxsubcat(request):
    cat= tbl_category.objects.get(id=request.GET.get("did"))
    subcat= tbl_subcategory.objects.filter(category=cat)
    return render(request,"Admin/AjaxSubcat.html",{"subcat":subcat,})

def galleryInsertselect(request):
    data=tbl_gallery.objects.all()
    category = tbl_category.objects.all()
    if request.method=="POST":
        description=request.POST.get('description')
        productphoto=request.FILES.get('productphoto')
        subcategory = tbl_subcategory.objects.get(id=request.POST.get('subcat'))
        product=tbl_product.objects.get(id=request.POST.get('sel_product'))
        tbl_gallery.objects.create(product_description=description,product_photo=productphoto,product_name=product,subcateg_name=subcategory)
        return render(request,"Admin/Gallery.html",{'data':data})
    else:
        return render(request,"Admin/Gallery.html",{'categorydata':category,})


def ajaxproduct(request):
    subcat = tbl_subcategory.objects.get(id=request.GET.get("did"))
    product = tbl_product.objects.filter(subcateg_name=subcat)
    return render(request,"Admin/AjaxProduct.html",{"productdata":product})


def ViewProductInsertSelect(request):
    data=tbl_product.objects.all()
    cat=tbl_category.objects.all()
    brand=tbl_brand.objects.all()
    subcat=tbl_subcategory.objects.all()
    if request.method=="POST":
        catd=tbl_category.objects.get(id=request.POST.get("sel_category"))
        brand=tbl_brand.objects.get(id=request.POST.get("sel_brand"))
        subcatd= tbl_subcategory.objects.get(id=request.POST.get("subcat"))
        data=tbl_product.objects.filter(subcateg_name=subcatd)
        return render(request,"Admin/ViewProduct.html" ,{'cat':cat,'subcat':subcat,'brand':brand,'product':data})
    else:
        return render(request,"Admin/ViewProduct.html",{'cat':cat,'subcat':subcat,'brand':brand,'product':data})


def Splistview(request):
    spdata = tbl_sp.objects.filter(sp_status=0)
    return render(request,"Admin/Splistview.html",{"spdata":spdata})

def Spaccept(request,aid):
    sp = tbl_sp.objects.get(id=aid)
    sp.sp_status = 1
    sp.save()
    return redirect("WebAdmin:LoadingHomePage")

def Spreject(request,rid):
    sp= tbl_sp.objects.get(id=rid)
    sp.sp_status = 2
    sp.save()
    return redirect("WebAdmin:LoadingHomePage")

def Spacceptedlist(request):
    spdata = tbl_sp.objects.filter(sp_status=1)
    return render(request,"Admin/Spaccept.html",{"spdata":spdata})

def Sprejectedlist(request):
    spdata = tbl_sp.objects.filter(sp_status=2)
    return render(request,"Admin/Spreject.html",{"spdata":spdata})


def ComplaintSelect(request):
    userdata=tbl_newuser.objects.all()
    data=tbl_complaint.objects.filter(complaint_status=0,user__in=userdata)
    return render(request,"Admin/NewComplaint.html",{'data':data})
    

def ComplaintReplyInsert(request,cid):
    complaint = tbl_complaint.objects.get(id=cid)
    if request.method=="POST":
        complaint.complaint_replydate = date.today()
        complaint.complaint_reply=request.POST.get('txtreply')
        complaint.complaint_status=1
        complaint.save()
        return redirect("WebAdmin:ComplaintSelect")
    else:
        return render(request,"Admin/ComplaintReply.html",{'complaint':complaint})

def ComplaintSolvedSelect(request):
    userdata=tbl_newuser.objects.all()
    data=tbl_complaint.objects.filter(complaint_status=1,user__in=userdata)
    return render(request,"Admin/SolvedComplaints.html",{'data':data})


def PanelbrandInsertSelect(request):
    data=tbl_panelbrand.objects.all()
    if request.method=="POST":
        pbrand=request.POST.get("txtpbrand")
        prate=request.POST.get("txtprate")
        tbl_panelbrand.objects.create(panelbrand_name=pbrand,panel_rate=prate)
        return render(request,"Admin/Panelbrand.html",{'data':data})
    else:
        return render(request,"Admin/Panelbrand.html",{'data':data})


def delpanelbrand(request,did):
    tbl_panelbrand.objects.get(id=did).delete()
    return redirect("WebAdmin:PanelbrandInsertSelect")

def Panelbrandupdate(request,eid):
    editdata=tbl_panelbrand.objects.get(id=eid)
    if request.method=="POST":
        editdata.panelbrand_name=(request.POST.get("txtpbrand"))
        editdata.panel_rate=(request.POST.get("txtprate"))
        editdata.save()
        return redirect("WebAdmin:PanelbrandInsertSelect")
    else:
        return render(request,"Admin/Panelbrand.html",{'editdata':editdata})

def InverterbrandInsertSelect(request):
    data=tbl_inverterbrand.objects.all()
    if request.method=="POST":
        ibrand=request.POST.get("txtibrand")
        irate=request.POST.get("txtirate")
        tbl_inverterbrand.objects.create(inverterbrand_name=ibrand,inverter_rate=irate)
        return render(request,"Admin/Inverterbrand.html",{'data':data})
    else:
        return render(request,"Admin/Inverterbrand.html",{'data':data})


def delinverterbrand(request,did):
    tbl_inverterbrand.objects.get(id=did).delete()
    return redirect("WebAdmin:InverterbrandInsertSelect")

def Inverterbrandupdate(request,eid):
    editdata=tbl_inverterbrand.objects.get(id=eid)
    if request.method=="POST":
        editdata.inverterbrand_name=(request.POST.get("txtibrand"))
        editdata.inverter_rate=(request.POST.get("txtirate"))
        editdata.save()
        return redirect("WebAdmin:InverterbrandInsertSelect")
    else:
        return render(request,"Admin/Inverterbrand.html",{'editdata':editdata})

def BatterybrandInsertSelect(request):
    data=tbl_batterybrand.objects.all()
    if request.method=="POST":
        bbrand=request.POST.get("txtbbrand")
        brate=request.POST.get("txtbrate")
        tbl_batterybrand.objects.create(batterybrand_name=bbrand,battery_rate=brate)
        return render(request,"Admin/Batterybrand.html",{'data':data})
    else:
        return render(request,"Admin/Batterybrand.html",{'data':data})


def delbatterybrand(request,did):
    tbl_batterybrand.objects.get(id=did).delete()
    return redirect("WebAdmin:BatterybrandInsertSelect")

def Batterybrandupdate(request,eid):
    editdata=tbl_batterybrand.objects.get(id=eid)
    if request.method=="POST":
        editdata.batterybrand_name=(request.POST.get("txtbbrand"))
        editdata.battery_rate=(request.POST.get("txtbrate"))
        editdata.save()
        return redirect("WebAdmin:BatterybrandInsertSelect")
    else:
        return render(request,"Admin/Batterybrand.html",{'editdata':editdata})





def PackageInsertSelect(request):
    data=tbl_package.objects.all()
    category=tbl_category.objects.all()
    pbrand=tbl_panelbrand.objects.all()
    ibrand=tbl_inverterbrand.objects.all()
    bbrand=tbl_batterybrand.objects.all()
    if request.method=="POST":
        package=request.POST.get("txtpackage")
        desc=request.POST.get("txtdesc")
        catid=tbl_category.objects.get(id=request.POST.get("sel_category"))
        pbrandid=tbl_panelbrand.objects.get(id=request.POST.get("sel_pbrand"))
        if request.POST.get("sel_ibrand"):
            ibrandid=tbl_inverterbrand.objects.get(id=request.POST.get("sel_ibrand"))
        else:
            ibrandid=""
        if request.POST.get("sel_bbrand"):
            bbrandid=tbl_batterybrand.objects.get(id=request.POST.get("sel_bbrand"))
        else:
            bbrandid=""
        power=request.POST.get("txtpower")
        amount=request.POST.get("txtamount")
        tbl_package.objects.create(package_name=package,package_photo=request.FILES.get("fileImage"),package_description=desc,category=catid,panel=pbrandid,inverter=ibrandid,battery=bbrandid,power=power,package_amount=amount)
        return render(request,"Admin/Package.html",{'data':data})
    else:
        return render(request,"Admin/Package.html",{'data':data,'category':category,'panelbrand':pbrand,'inverterbrand':ibrand,'batterybrand':bbrand})


def delPackage(request,did):
    tbl_package.objects.get(id=did).delete()
    return redirect("WebAdmin:PackageInsertSelect")

def Packageupdate(request,eid):
    editdata=tbl_package.objects.get(id=eid)
    category=tbl_category.objects.all()
    pbrand=tbl_panelbrand.objects.all()
    ibrand=tbl_inverterbrand.objects.all()
    bbrand=tbl_batterybrand.objects.all()
    if request.method=="POST":
        editdata.package_name=(request.POST.get("txtpackage"))
        editdata.package_photo=request.FILES.get("fileImage")
        editdata.package_description=(request.POST.get("txtdesc"))
        catid=tbl_category.objects.get(id=request.POST.get("sel_category"))
        pbrandid=tbl_panelbrand.objects.get(id=request.POST.get("sel_pbrand"))
        ibrandid=tbl_inverterbrand.objects.get(id=request.POST.get("sel_ibrand"))
        bbrandid=tbl_batterybrand.objects.get(id=request.POST.get("sel_bbrand"))
        editdata.power=(request.POST.get("txtpower"))
        editdata.package_amount=(request.POST.get("txtamount"))
        editdata.save()
        return redirect("WebAdmin:PackageInsertSelect")
    else:
        return render(request,"Admin/Package.html",{'editdata':editdata,'category':category,'panelbrand':pbrand,'inverterbrand':ibrand,'batterybrand':bbrand})


def PackageInterestSelect(request):
    userdata=tbl_newuser.objects.all()
    data=tbl_packageinterest.objects.filter(packageinterest_status=0)
    return render(request,"Admin/Userpackageinterest.html",{'data':data})


def PIReplyInsert(request,cid):
    packageinterest = tbl_packageinterest.objects.get(id=cid)
    if request.method=="POST":
        packageinterest.packageinterest_replydate = date.today()
        packageinterest.packageinterest_reply=request.POST.get('txtquote')
        quotation=request.FILES.get('Quotation')
        packageinterest.packageinterest_status=1
        packageinterest.quote_file=quotation
        packageinterest.save()
        return redirect("WebAdmin:PackageInterestSelect")
    else:
        return render(request,"Admin/PIreply.html",{'packageinterest':packageinterest})


def Quotationsend(request):
    userdata=tbl_newuser.objects.all()
    data=tbl_packageinterest.objects.filter(packageinterest_status=1)
    return render(request,"Admin/Quotationsenddetails.html",{'data':data})

def Paidorders(request):
    userdata=tbl_newuser.objects.all()
    data=tbl_packageinterest.objects.filter(packageinterest_status=1)
    return render(request,"Admin/Paidorders.html",{'data':data})

def Assignorder(request,eid):
    editdata=tbl_packageinterest.objects.get(id=eid)
    userID=tbl_newuser.objects.get(id=request.session["uid"])
    sp=tbl_sp.objects.all()
    if request.method=="POST":
        message=request.POST.get("txtmessage")
        sp=tbl_sp.objects.get(id=request.POST.get("sp"))
        tbl_assignorder.objects.create(assign_message=message,sp=sp,packageinterest=editdata,user=userID)
        return redirect("WebAdmin:index")
    else:
        return render(request,"Admin/Assignorder.html",{'editdata':editdata,'sp':sp})


def Assignedlistview(request):
    userdata=tbl_newuser.objects.all()
    data=tbl_assignorder.objects.filter(assign_status=0)
    return render(request,"Admin/Assignedlist.html",{'data':data})





def Installations(request):
    userdata=tbl_newuser.objects.all()
    package=tbl_package.objects.all()
    data=tbl_assignorder.objects.filter(assign_status=1)
    return render(request,"Admin/Installations.html",{'data':data})


def CRview(request):
    userdata=tbl_newuser.objects.all()
    data=tbl_customisedrequests.objects.filter(cr_status=0)
    return render(request,"Admin/CRview.html",{'data':data})

def CRReplyInsert(request,cid):
    customisedrequests = tbl_customisedrequests.objects.get(id=cid)
    if request.method=="POST":
        customisedrequests.customisedrequests_replydate = date.today()
        customisedrequests.customisedrequests_reply=request.POST.get('txtquote')
        customisedrequests.cramount=request.POST.get('txtamt')
        quotation=request.FILES.get('Quotation')
        customisedrequests.cr_status=1
        customisedrequests.quote_file=quotation
        customisedrequests.save()
        return redirect("WebAdmin:CRview")
    else:
        return render(request,"Admin/CRReply.html",{'customisedrequests':customisedrequests})

def PaidCRorders(request):
    userdata=tbl_newuser.objects.all()
    data=tbl_customisedrequests.objects.filter(cr_status=1)
    return render(request,"Admin/PaidCRorders.html",{'data':data})

def AssignCRorder(request,eid):
    editdata=tbl_customisedrequests.objects.get(id=eid)
    userID=tbl_newuser.objects.get(id=request.session["uid"])
    sp=tbl_sp.objects.all()
    if request.method=="POST":
        message=request.POST.get("txtmessage")
        sp=tbl_sp.objects.get(id=request.POST.get("sp"))
        tbl_crassignorder.objects.create(crassign_message=message,sp=sp,customisedrequests=editdata,user=userID)
        return redirect("WebAdmin:index")
    else:
        return render(request,"Admin/AssignCRorder.html",{'editdata':editdata,'sp':sp})

def CRAssignedlistview(request):
    userdata=tbl_newuser.objects.all()
    data=tbl_crassignorder.objects.filter(crassign_status=0)
    return render(request,"Admin/CRAssignedlist.html",{'data':data})

def CRInstallations(request):
    userdata=tbl_newuser.objects.all()
    data=tbl_crassignorder.objects.filter(crassign_status=1)
    return render(request,"Admin/CRInstallations.html",{'data':data})

def index(request):
    if request.method == "POST":
        return render(request, "Admin/adminindex.html")
    else:
        return render(request, "Admin/adminindex.html")

def feedbackSelect(request):
    data=tbl_feedback.objects.filter(user=request.session["uid"])
    return render(request,"Admin/FeedbackView.html",{'data':data})

def feedbackDelete(request,did):
    tbl_feedback.objects.get(id=did).delete()
    return redirect("WebAdmin:feedbackSelect")

def ajaxplace1(request):
    dis = tbl_district.objects.get(id=request.GET.get("did"))
    place = tbl_place.objects.filter(district_name=dis)
    return render(request,"Admin/AjaxPlace1.html",{"place":place})

def SpInsertSelect1(request):
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
        return render(request,"Admin/Spreg1.html",{'data':data})
    else:
        return render(request,"Admin/Spreg1.html",{'data':data,'district':district,'place':place})


def Report(request):
    if request.method=="POST":
        fromdate=request.POST.get("txtfromdate")
        todate=request.POST.get("txttodate")
        data=tbl_assignorder.objects.filter(assign_date__gte=fromdate,assign_date__lte=todate)
        return render(request,"Admin/Report.html",{'data':data})
    else:
        return render(request,"Admin/Report.html")

def Report2(request):
    if request.method=="POST":
        fromdate=request.POST.get("txtfromdate")
        todate=request.POST.get("txttodate")
        data=tbl_crassignorder.objects.filter(crassign_date__gte=fromdate,crassign_date__lte=todate)
        return render(request,"Admin/Report2.html",{'data':data})
    else:
        return render(request,"Admin/Report2.html")