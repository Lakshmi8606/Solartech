from django.db import models

# Create your models here.

class tbl_team(models.Model):
    team_name=models.CharField(max_length=50)
    team_flag=models.CharField(max_length=50)

class tbl_pcategory(models.Model):
    pcategory_name=models.CharField(max_length=50)

class tbl_player(models.Model):
    player_name=models.CharField(max_length=50)
    player_dob=models.CharField(max_length=50)
    player_photo=models.FileField(upload_to='Assets/playerimage/')
    team_name=models.ForeignKey(tbl_team,on_delete=models.CASCADE)
    pcategory_name=models.ForeignKey(tbl_pcategory,on_delete=models.CASCADE)

class tbl_match(models.Model):
    match_name=models.CharField(max_length=50)
    match_from=models.CharField(max_length=50)
    match_to=models.CharField(max_length=50)
    match_vanue=models.CharField(max_length=50)
   

