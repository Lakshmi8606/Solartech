from django.urls import path,include
from Basics import views
urlpatterns = [
    path('addition/',views.Sum),
    path('cal/',views.Calculator),
    path('large/',views.Largest),
    path('Ranklist/',views.Ranklist,name="Ranklist"),
    path('Salary/',views.Salary,name="Salary"),
   
]
