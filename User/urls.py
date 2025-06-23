from django.urls import path,include
from User import views

app_name="User"

urlpatterns = [

    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    
    path('ViewProduct/',views.ViewProductInsertSelect,name="ViewProductInsertSelect"),

    path('POSTComplaint/',views.POSTComplaint,name="POSTComplaint"),
    path('delComplaint/<int:did>', views.delComplaint,name="delComplaint"),
    path('ComplaintUpdate/<int:eid>', views.ComplaintUpdate,name="ComplaintUpdate"),
    path('Replyview/',views.Replyview,name="Replyview"),

    path('Viewpackage/',views.Viewpackage,name="Viewpackage"),

    path('Sendinterest/<int:eid>', views.Sendinterest,name="Sendinterest"),
    path('MI/',views.MyInterest,name="MyInterest"),
    path('Viewquote/',views.Viewquote,name="Viewquote"), 
    path('Qsendlist/',views.Quotationsendlist,name="Quotationsendlist"),   
    path('Payment/<int:id>',views.Payment,name="Payment"),   
    path('AssignedSp/',views.AssignedSp,name="AssignedSp"),
    path('index/',views.index,name="index"),

   
    path('CusrequestsInsertSelect/',views.CusrequestsInsertSelect,name="CusrequestsInsertSelect"),
    path('CRquoteview/',views.CRquoteview,name="CRquoteview"),  
    path('CRPayment/<int:id>',views.CRPayment,name="CRPayment"),
    path('AssignedCRSp/',views.AssignedCRSp,name="AssignedCRSp"),

    path('feedbackInsert/',views.feedbackInsert,name="feedbackInsert"),
    path('Userreport/',views.Userreport,name="Userreport"),
    path('Bill/<int:id>',views.Bill,name="Bill"),
]