from django.contrib import admin
from .models import * #Products, Category, Customer, CartOrder, CartOrderItems

admin.site.site_header  =  "Pompe funebre Rema admin"  
admin.site.site_title  =  "Pompe funebre Rema admin site"
admin.site.index_title  =  "Pompe funebre Rema Admin"

class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
admin.site.register(Products,AdminProduct)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Category)

class CustomerAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','phone','email','password')
admin.site.register(Customer,CustomerAdmin)


#orderItems
class OrdersAdmin(admin.ModelAdmin):
    list_display=('product','customer','feu','ne','decede','dateCeremony','name', 'image_tag','quantity','price','avance','morgue','paid_status')
admin.site.register(Orders,OrdersAdmin)

'''

class OrdersAdmin(admin.ModelAdmin):
    list_display=('product','customer','feu','ne','decede','dateCeremony','name', 'image','quantity','price','morgue','avance','paid_status')
admin.site.register(Orders,OrdersAdmin)

class OrdersAdminItems(admin.ModelAdmin):
    list_display=('product','customer','feu','ne','decede','dateCeremony','item', 'image','quantity','price','morgue','avance','paid_status')
admin.site.register(Orders,OrdersAdmin)
'''

# username = munyeshaka, email = muai@biu.bi, password = Aima_8080

