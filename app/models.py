from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()
  subject = models.TextField()
  message = models.TextField()
  add_on = models.DateTimeField(auto_now_add=True)
  is_apporved =models.BooleanField(default=True)

  def __str__(self):
    return self.name
  
  class Meta:
     verbose_name_plural = "Contact table"

class Profile(models.Model):
   user =models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
   address = models.TextField(blank=True)
   updated_on =models.DateTimeField(auto_now=True)

   def __str__(self):
        return self.user.username
   
   class Meta:
      verbose_name_plural = "Profile table"

class Car(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    image = models.FileField(null=True, blank=True, upload_to="images/",default=None,max_length=250)
    description = models.TextField(null=True, blank=True)
    price = models.CharField(max_length=100, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Order(models.Model) :
    order_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=90,default="")
    email = models.CharField(max_length=50,default="")
    phone = models.CharField(max_length=20,default="")
    address = models.CharField(max_length=500,default="")
    city = models.CharField(max_length=50,default="")
    cars = models.CharField(max_length=50,default="")
    days_for_rent = models.IntegerField(default=0)
    date = models.CharField(max_length=50,default="")
    loc_from = models.CharField(max_length=50,default="")
    loc_to = models.CharField(max_length=50,default="")
    
    def __str__(self):
        return self.name
        
    class Meta:
      verbose_name_plural = "Order table"

