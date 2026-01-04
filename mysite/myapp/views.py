from django.shortcuts import render ,get_object_or_404, redirect, HttpResponse,reverse
from django.http import JsonResponse,HttpResponseNotFound
from .models import Product,OrderDetail
import stripe ,json
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .forms import ProductForm , UserRegistrationForm
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta 
# Create your views here.


# to display the products in templtes 
def Product_list(request):
    products=Product.objects.all(  )
    return render(request,'myapp/index.html' ,{'products':products})



# to display product details and stripe payment gateway integration
def Product_details(request,id):
    product=Product.objects.get(id=id)
    stripe_publishable_key=settings.STRIPE_PUBLISHABLE_KEY
    return render(request,'myapp/details.html',{'product':product ,'stripe_publishable_key':stripe_publishable_key})


# to display product details and stripe payment gateway integration

def create_checkout_session(request, id):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid request"}, status=400)

    data = json.loads(request.body)
    product = get_object_or_404(Product, id=id)

    stripe.api_key = settings.STRIPE_SECRET_KEY

    checkout_session = stripe.checkout.Session.create(
        customer_email=data['email'],
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {'name': product.name},
                'unit_amount': int(product.price * 100),
            },
            'quantity': 1,
        }],
        mode='payment',
        # Stripe session ID will be appended to this URL
                success_url=request.build_absolute_uri(
            reverse('success')
        ) + "?session_id={CHECKOUT_SESSION_ID}",

        cancel_url=request.build_absolute_uri(reverse('failed')),
    )


    OrderDetail.objects.create(
    customer_email=data['email'],
    product=product,
    amount=int(product.price * 100),
    stripe_session_id=checkout_session.id  
)


    return JsonResponse({'sessionId': checkout_session.id})




#create success view 
def payment_success(request):
    session_id=request.GET.get('session_id')
    if session_id is None:
        return HttpResponseNotFound("Session ID not found")
    # Retrieve the session from Stripe
    stripe.api_key=settings.STRIPE_SECRET_KEY
    session=stripe.checkout.Session.retrieve(session_id)
    order=get_object_or_404(OrderDetail, stripe_session_id=session.id)
    order.has_paid=True
    #calculate  the  total sales of products
    product=Product.objects.get(id=order.product.id)
    product.total_sales_amount += int(product.price)
    #count the number of product is order  
    product.total_order+=1
    product.save()
    order.save()

    return render(request,'myapp/success.html',{'order':order})


#create failed view
def payment_failed(request):
    return render (request,'myapp/failed.html')


# view for user add products
def create_product(request):
    if request.method=='POST':
        product_form=ProductForm(request.POST ,request.FILES)
        if product_form.is_valid():
            #its save objects but not save final data  in the db because we want the seller field for each product form each seller   
            new_product=product_form.save(commit=False)
            new_product.seller=request.user
            #now new product is created along with the seller name or id 
            new_product.save()
            return redirect('index')
        else:
            print(product_form.errors)  
    product_form=ProductForm()
    return render (request,'myapp/create_product.html' ,{'product_form':product_form})



#create a view for edit the products

def edit_product(request,id):
    product=Product.objects.get(id=id)
    #check if the seller is login then allow to acces the edit 
    if product.seller != request.user:
        return redirect('invalid')
    product_form=ProductForm(request.POST or None, request.FILES or None , instance=product)
    if request.method=='POST':
        product_form=ProductForm(request.POST ,request.FILES,instance=product)
        if product_form.is_valid():
            product_form.save()
            return redirect('index')
    return render (request,'myapp/product_edit.html' ,{'product_form':product_form ,'product':product})


# create a view for delete 

def delete_product(request,id):
    product=Product.objects.get(id=id)
    if product.seller != request.user:
        return redirect('invalid')
    if request.method=="POST":
        product.delete()
        return redirect('index')


    return render(request,"myapp/delete_product.html",{'product':product})


# create a deshboard for handle products

def dashboard(request):
    #display the product only which i create in dashboard we can not see other user product 
    product=Product.objects.filter(seller=request.user)
    return render(request,'myapp/dashboard.html',{'products':product})



# view for  register 
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('index')
    else:
        user_form = UserRegistrationForm()

    return render(request, 'myapp/register.html', {'user_form': user_form})



def invalid(request):
    return render (request,"myapp/invalid.html")




def my_purchases(request):
    # get all the orders current login user purchases 
    orders=OrderDetail.objects.filter(customer_email=request.user.email)
    return render (request,'myapp/purchases.html' ,{'orders':orders})


#for calculate the total amount of product of the login user 
def sales_dashboard(request):
    #get all orders 
    orders=OrderDetail.objects.filter(product__seller=request.user)
    total_sales=orders.aggregate(Sum('amount'))

    print(total_sales)
    now = timezone.now()

    # calculate 365 days sales  
    last_year = now - timedelta(days=365)
    yearly_sales = orders.filter(created_on__gte=last_year).aggregate(Sum('amount'))

    # calculate 30 days sales  
    last_month = now - timedelta(days=30)
    monthly_sales = orders.filter(created_on__gte=last_month).aggregate(Sum('amount'))
    
    # calculate last 7 days sales  
    last_week = now - timedelta(days=7)
    weekly_sales = orders.filter(created_on__gte=last_week).aggregate(Sum('amount'))

    #every day sum past 30 days 
    daily_sales_sums=OrderDetail.objects.filter(product__seller=request.user).values('created_on').order_by('created_on').annotate(sum=Sum('amount'))
    # print(daily_sales_sums)

    #calculate per product sales 
    per_product_sales_sums=OrderDetail.objects.filter(product__seller=request.user).values('product__name').order_by('product__name').annotate(sum=Sum('amount'))
    # print(per_product_sales_sums)



    return render (request,'myapp/sales_dashboard.html',{'total_sales':total_sales , 'yearly_sales':yearly_sales ,'monthly_sales':monthly_sales ,'weekly_sales':weekly_sales,'daily_sales_sums':daily_sales_sums ,'per_product_sales_sums':per_product_sales_sums})