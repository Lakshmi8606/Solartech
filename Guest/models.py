from django.db import models
from Admin.models import *

# Create your models here.

class tbl_newuser(models.Model):
    user_name=models.CharField(max_length=50)
    user_gender=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_password=models.CharField(max_length=50)
    place_name=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    user_photo = models.FileField(upload_to='Assets/UserPhoto/')
    user_proof = models.FileField(upload_to='Assets/UserProof/')
    user_status = models.IntegerField(default="0")


class tbl_sp(models.Model):
    sp_name=models.CharField(max_length=50)
    sp_gender=models.CharField(max_length=50)
    sp_contact=models.CharField(max_length=50)
    sp_email=models.CharField(max_length=50)
    sp_password=models.CharField(max_length=50)
    place_name=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    sp_photo = models.FileField(upload_to='Assets/UserPhoto/')
    sp_proof = models.FileField(upload_to='Assets/UserProof/')
    sp_qualification=models.CharField(max_length=50)
    sp_status = models.IntegerField(default="0")

class tbl_complaint(models.Model):
    complaint_name=models.CharField(max_length=500)
    complaint_content=models.CharField(max_length=500)
    complaint_postdate=models.DateField(auto_now_add=True)
    complaint_reply=models.CharField(max_length=500)
    complaint_replydate=models.DateField(null=True)
    complaint_status = models.IntegerField(default="0")
    user = models.ForeignKey(tbl_newuser, on_delete=models.CASCADE,null=True)



class tbl_packageinterest(models.Model):
    package=models.ForeignKey(tbl_package, on_delete=models.CASCADE)
    packageinterest_date=models.DateField(auto_now_add=True)
    user = models.ForeignKey(tbl_newuser, on_delete=models.CASCADE,null=True)
    packageinterest_msg=models.CharField(max_length=50)
    packageinterest_status = models.IntegerField(default="0")
    packageinterest_pstatus = models.IntegerField(default="0")
    packageinterest_reply=models.CharField(max_length=500)
    packageinterest_replydate=models.DateField(null=True)
    quote_file = models.FileField(upload_to='Assets/Quotation/')


class tbl_customisedrequests(models.Model):
    subject=models.CharField(max_length=50)
    system=models.CharField(max_length=50)
    user=models.ForeignKey(tbl_newuser, on_delete=models.CASCADE)
    cr_status = models.IntegerField(default="0")
    category=models.ForeignKey(tbl_category, on_delete=models.CASCADE)
    panel=models.ForeignKey(tbl_panelbrand, on_delete=models.CASCADE)
    inverter=models.ForeignKey(tbl_inverterbrand, on_delete=models.CASCADE)
    battery=models.ForeignKey(tbl_batterybrand, on_delete=models.CASCADE)
    customisedrequests_date=models.DateField(auto_now_add=True)
    customisedrequests_reply=models.CharField(max_length=500)
    customisedrequests_replydate=models.DateField(null=True)
    cramount=models.CharField(max_length=50)
    customisedrequests_pstatus = models.IntegerField(default="0")
    customisedrequests_msg=models.CharField(max_length=50)

class tbl_assignorder(models.Model):
    assign_date=models.DateField(auto_now_add=True)
    packageinterest=models.ForeignKey(tbl_packageinterest, on_delete=models.CASCADE)
    user = models.ForeignKey(tbl_newuser, on_delete=models.CASCADE,null=True)
    sp=models.ForeignKey(tbl_sp, on_delete=models.CASCADE)
    assign_message=models.CharField(max_length=50)
    assign_status = models.IntegerField(default="0")

class tbl_crassignorder(models.Model):
    crassign_date=models.DateField(auto_now_add=True)
    customisedrequests=models.ForeignKey(tbl_customisedrequests, on_delete=models.CASCADE)
    user = models.ForeignKey(tbl_newuser, on_delete=models.CASCADE,null=True)
    sp=models.ForeignKey(tbl_sp, on_delete=models.CASCADE)
    crassign_message=models.CharField(max_length=50)
    crassign_status = models.IntegerField(default="0")
    

class tbl_feedback(models.Model):
    feedback_subject=models.CharField(max_length=500)
    feedback_details=models.CharField(max_length=500)
    feedback_postdate=models.DateField(auto_now_add=True)
    feedback_status = models.IntegerField(default="0")
    user = models.ForeignKey(tbl_newuser, on_delete=models.CASCADE)
