from django.urls import path,include
from Test import views

app_name="WebTest"

urlpatterns = [

    path('Team/',views.TeamInsertSelect,name="TeamInsertSelect"),
    path('delTeam/<int:did>', views.delTeam,name="delTeam"),
    path('updateTeam/<int:eid>', views.updateTeam,name="updateTeam"),

    path('PCategory/',views.PCategoryInsertSelect,name="PCategoryInsertSelect"),
    path('delPcategory/<int:did>', views.delPCategory,name="delPCategory"),
    path('updatePCategory/<int:eid>', views.updatePCategory,name="updatePCategory"),

    path('PDetails/',views.PlayerInsertSelect,name="PlayerInsertSelect"),
    path('Match/',views.MatchInsertSelect,name="MatchInsertSelect"),


    
]