from django.db import models

# Create your models here.
class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)

class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    district_name=models.ForeignKey(tbl_district,on_delete=models.CASCADE)



class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_contact=models.CharField(max_length=50)
    admin_email=models.CharField(max_length=50)
    admin_password=models.CharField(max_length=50)

class tbl_category(models.Model):
    category_name=models.CharField(max_length=50)


class tbl_panelbrand(models.Model):
    panelbrand_name=models.CharField(max_length=50)
    panel_rate=models.CharField(max_length=50)

class tbl_inverterbrand(models.Model):
    inverterbrand_name=models.CharField(max_length=50)
    inverter_rate=models.CharField(max_length=50)

class tbl_batterybrand(models.Model):
    batterybrand_name=models.CharField(max_length=50)
    battery_rate=models.CharField(max_length=50)


class tbl_package(models.Model):
    package_name=models.CharField(max_length=50)
    package_description=models.CharField(max_length=50)
    package_amount=models.CharField(max_length=50)
    package_msg=models.CharField(max_length=50)
    power=models.CharField(max_length=50)
    category=models.ForeignKey(tbl_category, on_delete=models.CASCADE)
    panel=models.ForeignKey(tbl_panelbrand, on_delete=models.CASCADE)
    inverter=models.ForeignKey(tbl_inverterbrand, on_delete=models.CASCADE,null=True)
    battery=models.ForeignKey(tbl_batterybrand, on_delete=models.CASCADE,null=True)
    package_photo =models.FileField(upload_to='Assets/packagephoto/')
    




    


    
    
    
    
    
    
   











    



    

