from django.urls import path,include
from Sp import views

app_name="Sp"

urlpatterns = [
    
    path('homepage/',views.homepage,name="homepage"),
    path('My_profile/',views.my_pro,name="my_pro"),
    path('editprofile/',views.editprofile,name="editprofile"),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('Myworks/',views.Myworks,name="Myworks"),
    path('Installstatus/<int:aid>', views.Installstatus,name="Installstatus"),
    path('MyCRworks/',views.MyCRworks,name="MyCRworks"),
    path('CRInstallstatus/<int:aid>', views.CRInstallstatus,name="CRInstallstatus"),
]