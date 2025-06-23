from django.shortcuts import render,redirect
from User.models import *
from Guest.models import *
from Admin.models import *



# Create your views here.

def homepage(request):
    return render(request,"User/HomePage.html")

def my_pro(request):
    data=tbl_newuser.objects.get(id=request.session["uid"])
    return render(request,"User/MyProfile.html",{'data':data})

def editprofile(request):
    prodata=tbl_newuser.objects.get(id=request.session["uid"])
    if request.method=="POST":
        prodata.user_name=request.POST.get('txtname')
        prodata.user_contact=request.POST.get('txtcon')
        prodata.user_email=request.POST.get('txtemail')
        prodata.save()
        return render(request,"User/EditProfile.html",{'msg':"Profile Updated"})
    else:
        return render(request,"User/EditProfile.html",{'prodata':prodata})

def changepassword(request):
    if request.method=="POST":
        ccount=tbl_newuser.objects.filter(id=request.session["uid"],user_password=request.POST.get('txtcurpass')).count()
        if ccount>0:
            if request.POST.get('txtnewpass')==request.POST.get('txtconpass'):
                userdata=tbl_newuser.objects.get(id=request.session["uid"],user_password=request.POST.get('txtcurpass'))
                userdata.user_password=request.POST.get('txtnewpass')
                userdata.save()
                return render(request,"User/ChangePassword.html",{'msg':"Password Updated"})
            else:
                return render(request,"User/ChangePassword.html",{'msg1':"Error in confirm Password"})
        else:
            return render(request,"User/ChangePassword.html",{'msg1':"Error in current password"})
    else:
        return render(request,"User/ChangePassword.html")


def ViewProductInsertSelect(request):
    data=tbl_product.objects.all()
    cat=tbl_category.objects.all()
    if request.method=="POST":
        cat=tbl_category.objects.get(id=request.POST.get("sel_category"))
        data=tbl_product.objects.filter(category_name=cat)
        return render(request,"User/ViewProduct.html" ,{'product':data})
    else:
        return render(request,"User/ViewProduct.html",{'cat':cat,'product':data})

def POSTComplaint(request):
    data=tbl_complaint.objects.filter(user=request.session["uid"])
    userID=tbl_newuser.objects.get(id=request.session["uid"])
    if request.method=="POST":
        name=request.POST.get('txtcomp')
        content=request.POST.get('txtcontent')
        tbl_complaint.objects.create(complaint_name=name,complaint_content=content,user=userID)
        return redirect("User:POSTComplaint")
    else:
        return render(request,"User/Complaint.html",{"data":data})
    
def delComplaint(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return redirect("User:POSTComplaint")

def ComplaintUpdate(request,eid):
    editdata=tbl_complaint.objects.get(id=eid)
    if request.method=="POST":
      editdata.complaint_name=(request.POST.get("txtcomp"))
      editdata.complaint_content=(request.POST.get("txtcontent"))
      editdata.save()
      return redirect("User:POSTComplaint")
    else:
      return render(request,"User/Complaint.html",{'editdata':editdata})


def Replyview(request):
    data=tbl_complaint.objects.filter(user=request.session["uid"])
    return render(request,"User/Replyview.html",{'data':data})


def Viewpackage(request):
    data=tbl_package.objects.all()
    return render(request,"User/Viewpackage.html",{'data':data})


def Sendinterest(request,eid):
    editdata=tbl_package.objects.get(id=eid)
    userID=tbl_newuser.objects.get(id=request.session["uid"])
    if request.method=="POST":
        message=request.POST.get("txtmessage")
        tbl_packageinterest.objects.create(packageinterest_msg=message,package=editdata,user=userID)
        return redirect("User:index")
    else:
        return render(request,"User/Sendinterest.html",{'editdata':editdata})

def MyInterest(request):
    data=tbl_newuser.objects.get(id=request.session["uid"])
    data=tbl_packageinterest.objects.filter(user=request.session["uid"])
    if request.method=="POST":
        data=tbl_packageinterest.objects.filter()
        return render(request,"User/Myinterests.html",{'data':data})
    else:
        return render(request,"User/Myinterests.html",{'data':data})


def Viewquote(request):
    data=tbl_packageinterest.objects.filter(user=request.session["uid"])
    return render(request,"User/Viewquote.html",{'data':data})


def Quotationsendlist(request):
    # data=tbl_newuser.objects.get(id=request.session["uid"])
    data=tbl_packageinterest.objects.filter(user=request.session["uid"],packageinterest_status=1)
    # userdata=tbl_newuser.objects.all()
    # data=tbl_packageinterest.objects.filter(packageinterest_status=1)
    return render(request,"User/Quotationsendlist.html",{'data':data})


def Payment(request,id):
    data = tbl_packageinterest.objects.get(id=id)
    userdata=tbl_package.objects.get(id=data.package_id)
    if request.method=="POST":
        data.packageinterest_pstatus=1
        data.save()
        return render(request,"User/index.html",{'msg':"Payment Successfull"})
    else:
        return render(request,"User/Payment.html",{'data':userdata})

def CRPayment(request,id):
    data = tbl_customisedrequests.objects.get(id=id)
    if request.method=="POST":
        data.customisedrequests_pstatus=1
        data.save()
        return render(request,"User/index.html",{'msg':"Payment Successfull"})
    else:
        return render(request,"User/Payment1.html",{'data':data})

def AssignedSp(request):
    data=tbl_newuser.objects.get(id=request.session["uid"])
    data=tbl_assignorder.objects.filter(user=request.session["uid"])
    if request.method=="POST":
        data=tbl_assignorder.objects.filter()
        return render(request,"User/AssignedSp.html",{'data':data})
    else:
        return render(request,"User/AssignedSp.html",{'data':data})


def index(request):
    if request.method == "POST":
        return render(request, "User/index.html")
    else:
        return render(request, "User/index.html")


def CusrequestsInsertSelect(request):
    user=tbl_newuser.objects.get(id=request.session["uid"])
    data=tbl_customisedrequests.objects.filter(user=user)
    category=tbl_category.objects.all()
    pbrand=tbl_panelbrand.objects.all()
    ibrand=tbl_inverterbrand.objects.all()
    bbrand=tbl_batterybrand.objects.all()
    if request.method=="POST":
        subject=request.POST.get("txtsubject")
        catid=tbl_category.objects.get(id=request.POST.get("sel_category"))
        pbrandid=tbl_panelbrand.objects.get(id=request.POST.get("sel_pbrand"))
        bbrandid=tbl_batterybrand.objects.get(id=request.POST.get("sel_bbrand"))
        ibrandid=tbl_inverterbrand.objects.get(id=request.POST.get("sel_ibrand"))
        power=request.POST.get("txtpower")
        tbl_customisedrequests.objects.create(subject=subject,system=power,category=catid,panel=pbrandid,battery=bbrandid,inverter=ibrandid,user=user)
        return render(request,"User/CusRequests.html",{'data':data})
    else:
        return render(request,"User/CusRequests.html",{'data':data,'category':category,'panelbrand':pbrand,'batterybrand':bbrand,'inverterbrand':ibrand})

def CRquoteview(request):
    data=tbl_customisedrequests.objects.filter(user=request.session["uid"],cr_status=1)
    return render(request,"User/CRquoteview.html",{'data':data})



def AssignedCRSp(request):
    data=tbl_newuser.objects.get(id=request.session["uid"])
    data=tbl_crassignorder.objects.filter(user=request.session["uid"])
    if request.method=="POST":
        data=tbl_crassignorder.objects.filter()
        return render(request,"User/AssignedCRSp.html",{'data':data})
    else:
        return render(request,"User/AssignedCRSp.html",{'data':data})

def feedbackInsert(request):
    if request.method=="POST":
        Subject=request.POST.get('txttitle')
        Content=request.POST.get('txtdetails')
        User=tbl_newuser.objects.get(id=request.session["uid"])
        tbl_feedback.objects.create(feedback_subject=Subject,feedback_details=Content,user=User)
        return render(request,"User/FeedbackPost.html")
    else:
        return render(request,"User/FeedbackPost.html")

def Userreport(request):
        data=tbl_packageinterest.objects.filter(user=request.session["uid"])
        return render(request,"User/Userreport.html",{'data':data})

def Bill(request,id):
    data=tbl_packageinterest.objects.get(id=id)
    prodata=tbl_newuser.objects.get(id=request.session["uid"])
    return render(request,"User/Bill.html",{'data':data,"prodata":prodata})
   