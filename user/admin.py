from django.contrib import admin
from user.models import Customer, Login, Category, SubCategory, Product, MainBanner, SubBanners1, SubBanners2, HeaderFlash
from user.models import  Wishlist, AddToCart, ChangePassword, Order, CashonDeliveyOrders
# Register your models here.
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Product)

admin.site.register(MainBanner)
admin.site.register(SubBanners1)
admin.site.register(SubBanners2)
admin.site.register(HeaderFlash)
admin.site.register(Login)
# admin.site.register(Cart)
admin.site.register(Wishlist)
admin.site.register(AddToCart)
admin.site.register(ChangePassword)

# admin.site.register(Coupon)
admin.site.register(Order)
admin.site.register(CashonDeliveyOrders)