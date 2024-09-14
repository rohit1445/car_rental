from django.contrib import admin
from app.models import Contact,Profile,Car,Order

# Register your models here.
admin.site.site_header = "RM CAR RENTAL | Admin"

class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','subject','message','add_on']

admin.site.register(Contact, ContactAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id','user','updated_on','address']
    
admin.site.register(Profile, ProfileAdmin)

class CarAdmin(admin.ModelAdmin):
    list_display = ['id','name','image','description','price','updated','created']
    
admin.site.register(Car, CarAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_id','name','address','cars','date','days_for_rent','phone','loc_from','loc_to']

admin.site.register(Order, OrderAdmin)

