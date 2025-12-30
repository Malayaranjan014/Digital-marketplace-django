from django.shortcuts import render ,get_object_or_404, redirect, HttpResponse,reverse
from django.http import JsonResponse,HttpResponseNotFound
from .models import Product,OrderDetail
import stripe ,json
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .forms import ProductForm , UserRegistrationForm

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
            product_form.save()
            return redirect('index')
        else:
            print(product_form.errors)  
    product_form=ProductForm()
    return render (request,'myapp/create_product.html' ,{'product_form':product_form})



#create a view for edit the products

def edit_product(request,id):
    product=Product.objects.get(id=id)
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
    if request.method=="POST":
        product.delete()
        return redirect('index')


    return render(request,"myapp/delete_product.html",{'product':product})


# create a deshboard for handle products

def dashboard(request):
    product=Product.objects.all()
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



