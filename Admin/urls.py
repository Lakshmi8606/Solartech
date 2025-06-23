from django.urls import path,include
from Admin import views

app_name="WebAdmin"

urlpatterns = [

    path('District/',views.DistrictInsertSelect,name="DistrictInsertSelect"),
    path('delDistrict/<int:did>', views.delDistrict,name="delDistrict"),
    path('Districtupdate/<int:eid>', views.Districtupdate,name="Districtupdate"),
    path('Place/',views.PlaceInsertSelect,name="PlaceInsertSelect"),
    path('delPlace/<int:did>', views.delPlace,name="delPlace"),
    path('Placeupdate/<int:eid>', views.Placeupdate,name="Placeupdate"),

    path('category/',views.CategoryInsertSelect,name="CategoryInsertSelect"),
    path('delcategory/<int:did>', views.delcategory,name="delcategory"),
    path('Categoryupdate/<int:eid>', views.Categoryupdate,name="Categoryupdate"),


    path('Adminreg/',views.Adminreg,name="Adminreg"),
    path('delAdminreg/<int:did>', views.delAdminreg,name="delAdminreg"),
    path('Adminregupdate/<int:eid>', views.Adminregupdate,name="Adminregupdate"),


    path('Userview/',views.UserviewInsertSelect,name="UserviewInsertSelect"),
    path('delUserview/<int:did>', views.delUserview,name="delUserview"),
    path('Userlistview/',views.Userlistview,name="Userlistview"),
    path('Useraccept/',views.Useraccept,name="Useraccept"),
    path('Userreject/',views.Userreject,name="Userreject"),
    path('Useracceptedlist/',views.Useracceptedlist,name="Useracceptedlist"),
    path('Userrejectedlist/',views.Userrejectedlist,name="Userrejectedlist"),
    path('Useraccept/<int:aid>',views.Useraccept,name="Useraccept"),
    path('Userreject/<int:rid>',views.Userreject,name="Userreject"),
    path('Homepage/',views.LoadingHomePage,name="LoadingHomePage"),
    

    path('Subcategory/',views.subcategRegistration,name="subcategRegistration"),
    path('delSubcateg/<int:did>', views.delSubcateg,name="delSubcateg"),
    path('Subcategupdate/<int:eid>',views.Subcategupdate,name="Subcategupdate"),

    path('Product/',views.ProductInsertSelect,name="ProductInsertSelect"),

    path('AjaxSubcat/',views.ajaxsubcat,name="ajaxsubcat"),

    path('Gallery/',views.galleryInsertselect,name="galleryInsertselect"),
    path('AjaxProduct/',views.ajaxproduct,name="ajaxproduct"),

    path('ViewProduct/',views.ViewProductInsertSelect,name="ViewProductInsertSelect"),

     path('Splistview/',views.Splistview,name="Splistview"),
    path('Spaccept/',views.Spaccept,name="Spaccept"),
    path('Spreject/',views.Spreject,name="Spreject"),
    path('Spacceptedlist/',views.Spacceptedlist,name="Spacceptedlist"),
    path('Sprejectedlist/',views.Sprejectedlist,name="Sprejectedlist"),
    path('Spaccept/<int:aid>',views.Spaccept,name="Spaccept"),
    path('Spreject/<int:rid>',views.Spreject,name="Spreject"),

    path('ComplaintView/',views.ComplaintSelect,name="ComplaintSelect"),
    path('ComplaintReply/<int:cid>',views.ComplaintReplyInsert,name="ComplaintReplyInsert"),
    path('ComplaintSolvedView/',views.ComplaintSolvedSelect,name="ComplaintSolvedSelect"),

    path('pbrand/',views.PanelbrandInsertSelect,name="PanelbrandInsertSelect"),
    path('delpbrand/<int:did>', views.delpanelbrand,name="delpanelbrand"),
    path('pbrandupdate/<int:eid>', views.Panelbrandupdate,name="Panelbrandupdate"),

    path('ibrand/',views.InverterbrandInsertSelect,name="InverterbrandInsertSelect"),
    path('delibrand/<int:did>', views.delinverterbrand,name="delinverterbrand"),
    path('ibrandupdate/<int:eid>', views.Inverterbrandupdate,name="Inverterbrandupdate"),

    path('bbrand/',views.BatterybrandInsertSelect,name="BatterybrandInsertSelect"),
    path('delbbrand/<int:did>', views.delbatterybrand,name="delbatterybrand"),
    path('bbrandupdate/<int:eid>', views.Batterybrandupdate,name="Batterybrandupdate"),

    path('Package/',views.PackageInsertSelect,name="PackageInsertSelect"),
    path('delPackage/<int:did>', views.delPackage,name="delPackage"),
    path('Packageupdate/<int:eid>', views.Packageupdate,name="Packageupdate"),

    path('PI/',views.PackageInterestSelect,name="PackageInterestSelect"),   
    path('PIReply/<int:cid>',views.PIReplyInsert,name="PIReplyInsert"),

    path('Quotationsend/',views.Quotationsend,name="Quotationsend"),

    path('Paidorders/',views.Paidorders,name="Paidorders"),
    path('Assignorder/<int:eid>', views.Assignorder,name="Assignorder"),
    path('Assignedlistview/',views.Assignedlistview,name="Assignedlistview"),

    

    path('Installations/',views.Installations,name="Installations"),
    path('CRview/',views.CRview,name="CRview"),
    path('CRReplyInsert/<int:cid>',views.CRReplyInsert,name="CRReplyInsert"),
    path('PaidCRorders/',views.PaidCRorders,name="PaidCRorders"),
    path('AssignCRorder/<int:eid>', views.AssignCRorder,name="AssignCRorder"),
    path('CRAssignedlistview/',views.CRAssignedlistview,name="CRAssignedlistview"),
    path('CRInstallations/',views.CRInstallations,name="CRInstallations"),

    path('index/',views.index,name="index"),
    path('feedbackSelect/',views.feedbackSelect,name="feedbackSelect"),
    path('feedbackDelete/<int:did>',views.feedbackDelete,name="feedbackDelete"),

    path('AjaxPlace1/',views.ajaxplace1,name="ajaxplace1"),
    path('Sp1/',views.SpInsertSelect1,name="SpInsertSelect1"),
    path('Report/',views.Report,name="Report"),
    path('Report2/',views.Report2,name="Report2"),
]
