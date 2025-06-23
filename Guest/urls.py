from django.urls import path,include
from Guest import views

app_name="WebGuest"

urlpatterns = [

    path('Newuser/',views.NewuserInsertSelect,name="NewuserInsertSelect"),
    path('AjaxPlace/',views.ajaxplace,name="ajaxplace"),
    path('Login/',views.Login,name="Login"),
    path('Sp/',views.SpInsertSelect,name="SpInsertSelect"),
    path('index/',views.index,name="index"),
]