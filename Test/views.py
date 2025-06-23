from django.shortcuts import render,redirect
from Test.models import *

# Create your views here.

def TeamInsertSelect(request):
    data=tbl_team.objects.all()
    if request.method=="POST":
        teamname=request.POST.get("txtname")
        teamflag=request.POST.get("txtflag")
        tbl_team.objects.create(team_name=teamname,team_flag=teamflag)
        return render(request,"Test/Team.html",{'data':data})
    else:
        return render(request,"Test/Team.html",{'data':data})


def delTeam(request,did):
    tbl_team.objects.get(id=did).delete()
    return redirect("WebTest:TeamInsertSelect")


def updateTeam(request,eid):
    editdata=tbl_team.objects.get(id=eid)
    if request.method=="POST":
        editdata.team_name=(request.POST.get("txtname"))
        editdata.team_flag=(request.POST.get("txtflag"))
        editdata.save()
        return redirect("WebTest:TeamInsertSelect")
    else:
        return render(request,"Test/Team.html",{'editdata':editdata})

def PCategoryInsertSelect(request):
    data=tbl_pcategory.objects.all()
    if request.method=="POST":
        pcatname=request.POST.get("txtname")
        tbl_pcategory.objects.create(pcategory_name=pcatname)
        return render(request,"Test/PlayerCategory.html",{'data':data})
    else:
        return render(request,"Test/PlayerCategory.html",{'data':data})


def delPCategory(request,did):
    tbl_pcategory.objects.get(id=did).delete()
    return redirect("WebTest:PCategoryInsertSelect")


def updatePCategory(request,eid):
    editdata=tbl_pcategory.objects.get(id=eid)
    if request.method=="POST":
        editdata.pcategory_name=(request.POST.get("txtname"))
        editdata.save()
        return redirect("WebTest:PCategoryInsertSelect")
    else:
        return render(request,"Test/PlayerCategory.html",{'editdata':editdata})


def PlayerInsertSelect(request):
    data=tbl_player.objects.all()
    team=tbl_team.objects.all()
    cat=tbl_pcategory.objects.all()
    if request.method=="POST":
        pname=request.POST.get("txtname")
        dob=request.POST.get("txtdate")
        team=tbl_team.objects.get(id=request.POST.get("sel_team"))
        cat=tbl_pcategory.objects.get(id=request.POST.get("cat"))
        tbl_player.objects.create(player_name=pname,player_dob=dob,player_photo=request.FILES.get("fileImage"),team_name=team,pcategory_name=cat)
        return render(request,"Test/PlayDetails.html",{'data':data})
    else:
        return render(request,"Test/PlayDetails.html",{'data':data,'team':team,'cat':cat})


def MatchInsertSelect(request):
    data=tbl_match.objects.all()
    if request.method=="POST":
        matchname=request.POST.get("txtname")
        fromdate=request.POST.get("txtfrom")
        todate=request.POST.get("txtto")
        matchvenue=request.POST.get("txtvenue")
        tbl_match.objects.create(match_name=matchname,match_from=fromdate,match_to=todate,match_vanue=matchvenue)
        return render(request,"Test/Schedule.html",{'data':data})
    else:
        return render(request,"Test/Schedule.html",{'data':data})