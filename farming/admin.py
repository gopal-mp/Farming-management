from django.contrib import admin
from farming.models import addseller,blockchainoutput,addworker,addcustomer,product,payment,usercategory,usernews,seller_request,userproduct,machinery,Order,cart

# Register your models here.
admin.site.register(addseller)
#admin.site.register(admin)
admin.site.register(blockchainoutput)
admin.site.register(addworker)
admin.site.register(addcustomer)
admin.site.register(product)
admin.site.register(payment)
admin.site.register(usercategory)
admin.site.register(usernews)
admin.site.register(seller_request)
admin.site.register(userproduct)
admin.site.register(machinery)
admin.site.register(Order)
admin.site.register(cart)



