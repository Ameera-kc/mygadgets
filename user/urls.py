from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("about-us", views.about_us, name="about_us"),
    path("cart/<int:id>", views.addtocart, name="addtocart"),
    path("cart", views.viewcart, name="viewcart"),
    path("checkout", views.checkout, name="checkout"),
    path("coming-soon", views.coming_soon, name="coming_soon"),
    path("contact-us", views.contact_us, name="contact_us"),
    path("faq", views.faq, name="faq"),
    path("forgot", views.forget_password, name="forgot password"),
    path('change password/<token>/', views.change_password, name="change password"),
    path("delete/<int:id>", views.deletefromwishlist, name="deletefromwishlist"),
    path("deletecart/<int:id>", views.deletefromcart, name="deletefromcart"),
    path("", views.index, name="index"),
    path("login", views.login_views, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("order--success", views.order_success2, name="order__success"),
    path("order-tracking", views.order_tracking, name="order_tracking"),
    path("otp", views.otp, name="otp"),
    path("product/<int:id>", views.product, name="product"),
    path("search", views.search, name="search"),
    path("seller-dashboard", views.seller_dashboard, name="seller_dashboard"),
    path("shop-category/<int:id>", views.shop_category, name="shop_category"),
    path("shop/<int:id>", views.shop, name="shop"),
    path("sign-up", views.user_register, name="sign_up"),
    path("dashboard", views.user_dashboard, name="dashboard"),
    path("wishlist/<int:id>", views.addtowishlist, name="addtowishlist"),
    path("wishlist",views.viewwishlist,name="viewwishlist"),
    path("404", views.error_404, name="error_404"),
    
    # cart add ajax
    path("addquantity/",views.addQuantity, name="addquantity"),
    path("lessquantity/",views.lessQuantity,name="lessquantity"),
    
    # payment
    path("payment/", views.order_payment, name="payment"),
    path("order_success/", views.callback, name="order_success"),
]
