from django.contrib import admin

from .models import Customer,Paytype,Admin,Roomtype,Ratings,Room,Bill,Booking,Billpay,Rent,Roomratings

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id','first_name','last_name')
admin.site.register(Paytype)
admin.site.register(Admin)
admin.site.register(Roomtype)
admin.site.register(Ratings)
admin.site.register(Rent)
admin.site.register(Room)


