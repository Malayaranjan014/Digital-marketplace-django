from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import CustomLoginForm


urlpatterns = [
    path('',views.Product_list,name='index'),
    path('product/<int:id>',views.Product_details,name="details"),
    path('success/',views.payment_success,name='success'),
    path('failed/',views.payment_failed,name='failed'),
    #when user click buy button this url will be called
    path('api/checkout-session/<int:id>/',views.create_checkout_session,name='checkout_session'),
    path('createproduct/',views.create_product,name='createproduct'),
    path('editproduct/<int:id>/',views.edit_product,name='editproduct'),
    path('deleteproduct/<int:id>/',views.delete_product,name='deleteproduct'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('register/',views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='myapp/login.html' ,authentication_form=CustomLoginForm),name="login"),
    path('logout/',auth_views.LogoutView.as_view() ,name="logout"),
    path('invalid/',views.invalid,name="invalid"),
    path('purchases/',views.my_purchases,name="purchases"),
    path('sales/',views.sales_dashboard,name='sales'), 
]