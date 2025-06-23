from django.shortcuts import render

# Create your views here.
def Sum(request):
    if request.method=="POST":
        num1=int(request.POST.get("number1"))
        num2=int(request.POST.get("number2"))
        sum=num1+num2
        return render(request,"Basics/Sum.html",{"Result":sum})
    else:
        return render(request,"Basics/Sum.html")
def Calculator(request):
    if request.method=="POST":
        num1=int(request.POST.get("Number1"))
        num2=int(request.POST.get("Number2"))
        btn=request.POST.get("num")
        if btn=="+":
            sum=num1+num2
            return render(request,"Basics/Calculator.html",{"Result":sum})
        elif btn=="-":
            diff=num1-num2
            return render(request,"Basics/Calculator.html",{"Result":diff})
        elif btn=="*":
            mul=num1*num2
            return render(request,"Basics/Calculator.html",{"Result":mul})
        elif btn=="/":
            div=num1/num2
            return render(request,"Basics/Calculator.html",{"Result":div})
    else:
        return render(request,"Basics/Calculator.html")
def Largest(request):
    largest=""
    if request.method=="POST":
        num1=int(request.POST.get("Number1"))
        num2=int(request.POST.get("Number2"))
        num3=int(request.POST.get("Number3"))
        if(num1>=num2) and (num1>=num3):
            largest=num1
        elif(num2>=num1) and (num2>=num3):
            largest=num2
        else:
            largest=num3
        return render(request,"Basics/Largest.html",{"Result":largest})
    else:
        return render(request,"Basics/Largest.html",{"Result":largest})
def Ranklist(request):
    name=""
    gender=""
    dept=""
    total=""
    per=""
    grade=""
    if request.method=="POST":
        fn=(request.POST.get("txtfname"))
        ln=(request.POST.get("txtlname"))

        gender=(request.POST.get("gender"))
        dept=(request.POST.get("Department"))

        m1=int(request.POST.get("txtm1"))
        m2=int(request.POST.get("txtm2"))
        m3=int(request.POST.get("txtm3"))

        name=fn+" "+ln
        total=m1+m2+m3
        per=total/3
        if(per>=80):
            grade="A"
        elif(per>=60):
            grade="B"
        elif(per>=50):
            grade="C"
        else:
            grade="D"
        return render(request,"Basics/Ranklist.html",{"name":name,"gender":gender,"dept":dept,"total":total,"per":per,"grade":grade})
    else:
        return render(request,"Basics/Ranklist.html",{"name":name,"gender":gender,"dept":dept,"total":total,"per":per,"grade":grade})
def Salary(request):
    name=""
    gender=""
    ms=""
    dept=""
    ta=""
    da=""
    hra=""
    lic=""
    pf=""
    ns=""
    if request.method=="POST":
        fn=request.POST.get("txtfn")      
        ln=request.POST.get("txtln")
        gender=request.POST.get("gender")
        ms=request.POST.get("btnms")  
        dept=request.POST.get("Department")
        bs=int(request.POST.get("txtbs"))
        name=fn+" "+ln
        if(bs>=25000):
            ta=bs*0.4
            da=bs*0.35
            hra=bs*0.3
            lic=bs*0.25
            pf=bs*0.2
            ns=bs+(da+ta+hra)-(lic+pf)
        elif(bs>=20000):
            ta=bs*0.35
            da=bs*0.3
            hra=bs*0.25
            lic=bs*0.2
            pf=bs*0.15
            ns=bs+(da+ta+hra)-(lic+pf)
        else:
            ta=bs*0.3
            da=bs*0.25
            hra=bs*0.2
            lic=bs*0.15
            pf=bs*0.1
            ns=bs+(da+ta+hra)-(lic+pf)
        return render(request,"Basics/Salary.html",{"name":name,"gender":gender,"marst":ms,"dept":dept,"ta":ta,"da":da,"hra":hra,"lic":lic,"pf":pf,"ns":ns})
    else:
        return render(request,"Basics/Salary.html",{"name":name,"gender":gender,"marst":ms,"dept":dept,"ta":ta,"da":da,"hra":hra,"lic":lic,"pf":pf,"ns":ns})







