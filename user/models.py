from django.db import models
from versatileimagefield.fields import VersatileImageField
from tinymce.models import HTMLField
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth.models import (
    AbstractUser,
 )

# Create your models here.


class Login(AbstractUser):
    is_customer = models.BooleanField(default=False)
    

class Customer(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='user')
    customer_name = models.CharField(max_length = 100,null=True)
    phone_number = models.CharField(default=0, null=True, max_length=10, unique = True)  
    email = models.EmailField(max_length=254,null=True)
    address = models.CharField(max_length = 250)
    
    def __str__(self):
        return self.customer_name

    
class Category(models.Model):
    category = models.CharField(max_length = 200, unique=True)
    image = VersatileImageField(upload_to="categories/", null=True)
    
    def get_absolute_url(self):
        return reverse_lazy("user:shop", kwargs={"id": self.id})
    
    def get_subcategories(self):
        return SubCategory.objects.filter(category=self) 
    
    def get_products(self):
        return Product.objects.filter(category=self)
         
    def __str__(self):
        return self.category
    
    
class SubCategory(models.Model):
    subcategory = models.CharField(max_length = 150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse_lazy("user:product", kwargs={"id": self.id})

    def get_shop_url(self):
        return reverse_lazy("user:shop", kwargs={"id": self.id})
    
    def get_products(self):
        return Product.objects.filter(subcategory=self) 
    
    def __str__(self):
        return self.subcategory
       

    
class Product(models.Model):
    product = models.CharField(max_length = 150)
    image = VersatileImageField(upload_to="products/", null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE,null=True, blank=True)
    price = models.IntegerField()
    offer_price = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(default = 0)
    description = models.CharField(max_length = 250)
    is_top_save_today= models.BooleanField(default = False,null=True, blank=True)
    is_best_seller = models.BooleanField(default = False,null=True, blank=True)
    sub_image1 = VersatileImageField(upload_to="products/", null=True, blank=True)
    sub_image2 = VersatileImageField(upload_to="products/", null=True, blank=True)
    sub_image3 = VersatileImageField(upload_to="products/", null=True, blank=True)
    
    
    def __str__(self):
        return self.product

    

class MainBanner(models.Model):
    bannerbig = VersatileImageField(upload_to="MainBanner/", null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE ,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=True)
    
    

class SubBanners1(models.Model):
    subbanner1 = VersatileImageField(upload_to="SubBanners/", null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE ,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=True)
    
  
    
class SubBanners2(models.Model):
    subbanner2 = VersatileImageField(upload_to="SubBanners/", null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE ,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=True)
    
    

class HeaderFlash(models.Model):
    address =  models.CharField(max_length = 150)
    offer_product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=True)
    
    def __str__(self):
        return self.address


class Wishlist(models.Model):
    user = models.ForeignKey(Customer,on_delete=models.CASCADE, null=True,default='')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,default='',null=True,blank=True)
    added_date = models.DateTimeField(auto_now_add=True)
       
    


class ChangePassword(models.Model):
    user = models.ForeignKey(Customer,on_delete=models.CASCADE, blank=True, null=True)
    forgot_password_token = models.CharField(max_length=100)
    created_at = models. DateTimeField(auto_now_add = True)
    status = models.BooleanField(default=False)

    def _str_(self):
        return str(self.user)
 
    
def get_absolute_url(self):
    return reverse("_detail", kwargs={"pk": self.pk})


# class Coupon(models.Model):
#     coupon_code = models.CharField(max_length=10)
#     is_expired = models.BooleanField(default=False)
#     discount_price = models.IntegerField(default=100)
#     minimum_amount = models.IntegerField(default=5000)
    
#     def __str__(self):
#         return self.coupon_code



# class Cart(models.Model):
#     user = models.ForeignKey(Customer,on_delete=models.CASCADE, null=True,default='')
#     is_paid = models.BooleanField(default = False)
    
    
    
#     def get_cart_total(self):
#         cart_items=self.cart_item.all()
#         price = []
#         for cart_item in cart_items:
#             price.append(cart_item.product.price)
            
        
#         if self.coupon:
#             return sum(price) - self.coupon.discount_price
#         return sum

#     def __str__(self):
#         return self.is_paid



class AddToCart(models.Model):
    user = models.ForeignKey(Customer,on_delete=models.CASCADE, null=True,default='')
    # coupon = models.ForeignKey(Coupon, on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)
    quantity=models.IntegerField(null=True, default=1 )
    total = models.IntegerField(null=True)
    
    
    def __str__(self):
        return self.user    



# payment


from django.db import models
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _
from .constants import PaymentStatus


class Order(models.Model):
    name = CharField(_("Customer Name"), max_length=254, blank=False, null=False)
    amount = models.FloatField(_("Amount"), null=False, blank=False)
    email = CharField(_("Email Address"), max_length=254, blank=True, null=True)
    landmark = CharField(_("Land Mark"), max_length=254, blank=True, null=True)
    address = CharField(_("Address"), max_length=254, blank=True, null=True)
    contact = models.FloatField(_("Contact"), null=True, blank=True)
    status = CharField(
        _("Payment Status"),
        default=PaymentStatus.PENDING,
        max_length=254,
        blank=False,
        null=False,
    )
    provider_order_id = models.CharField(
        _("Order ID"), max_length=40, null=False, blank=False
    )
    payment_id = models.CharField(
        _("Payment ID"), max_length=36, null=False, blank=False
    )
    signature_id = models.CharField(
        _("Signature ID"), max_length=128, null=False, blank=False
    )

    def __str__(self):
        return f"{self.id}-{self.name}-{self.status}"


class CashonDeliveyOrders(models.Model):
    name = CharField(_("Customer Name"), max_length=254, blank=False, null=False)
    amount = models.FloatField(_("Amount"), null=False, blank=False)
    email = CharField(_("Email Address"), max_length=254, blank=True, null=True)
    landmark = CharField(_("Land Mark"), max_length=254, blank=True, null=True)
    address = CharField(_("Address"), max_length=254, blank=True, null=True)
    contact = models.FloatField(_("Contact"), null=True, blank=True)
    
    
    
    def __str__(self):
        return self.name 