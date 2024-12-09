from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from rest_framework.response import Response
from .forms import CreateUserForm
from rest_framework import viewsets
from . models import Task
from .forms import ProductForm
from django.contrib import messages
from .models import Product
from .serializers import TaskSerializer
from .serializers import ProductSerializer, PricingSerializer, CustomerSerializer, TaskSerializer

from .models import Product, Pricing, Customer, Slider, Services, Details, Recent, Post, Testimonials, Test, Json, Icon, \
    Moon, About, New, Section, Excel, Cart, Events, Feedback, Discount, Author, Profile, Main, Support, List, List_desc, \
    Pixel, Php, Comment, Shop, Employee, Update, Apply, Special, Alx, Redeem, User, Order, Contact, Hours, Our

#  CRUD.
# View all products
def view_products(request):
    products = Product.objects.all()
    return render(request, 'view_products.html', {'products': products})

# Add new product
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_products')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

# View to add a new product
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_products')
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})

# View to edit a product
def edit_product(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == 'POST':
        # Update the product from the submitted form data
        product.prod_name = request.POST.get('prod_name')
        product.prod_price = request.POST.get('prod_price')
        product.prod_category = request.POST.get('prod_category')
        product.prod_qty = request.POST.get('prod_qty')
        product.prod_desc = request.POST.get('prod_desc')

        # Handle image upload (optional)
        if request.FILES.get('prod_img'):
            product.prod_img = request.FILES['prod_img']

        product.save()
        return redirect('view_products')

    return render(request, 'edit_product.html', {'product': product})

# Delete product
def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "POST":
        product.delete()
        return redirect('view_products')
    return render(request, 'delete_product.html', {'product': product})
#ENDCRUD

def subscribe(request):
    if request.method == "POST":
        email = request.POST.get('email')
        messages.success(request, "Thank you for your subscription!")
        return redirect('home')
    return redirect('home')

#DROPDOWN
def fertilizers(request):
    return render(request, 'fertilizers.html')

def farming_tools(request):
    return render(request, 'farming_tools.html')

def pesticides(request):
    return render(request, 'pesticides.html')

def irrigation_equipments(request):
    return render(request, 'irrigation_equipments.html')

def livestock_supply(request):
    return render(request, 'livestock_supply.html')
#ENDDROPDOWN

# ViewSets
class ProductsView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PricingViewSet(viewsets.ModelViewSet):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
#ENDVIEWSETS

# Views
def home(request):
    sliders = Slider.objects.all()
    services = Services.objects.first()
    details = Details.objects.all()
    recent = Recent.objects.first()
    post = Post.objects.all()
    testimonials = Testimonials.objects.first()
    test = Test.objects.all()
    json = Json.objects.all()
    icon = Icon.objects.first()
    moon = Moon.objects.first()
    about = About.objects.first()
    new = New.objects.all()
    update = Update.objects.all()
    order = Order.objects.all()
    products = Product.objects.all()
    customers = Customer.objects.all()
    context = {
        'sliders': sliders,
        'services': services,
        'details': details,
        'recent': recent,
        'post': post,
        'testimonials': testimonials,
        'test': test,
        'json': json,
        'icon': icon,
        'moon': moon,
        'about': about,
        'new': new,
        'update': update,
        'order': order,
        'products': products,
        'customers': customers,
    }
    return render(request, 'index.html', context)


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'register.html', {'form': form})

def login(request):
    context ={}
    return render(request, 'login.html', context)

def view_products(request):
    products = Product.objects.all()
    return render(request, 'view_products.html', {'products': products})

def insert_data(request):
    if request.method == "POST":
        prod_name = request.POST['prod_name']
        prod_price = request.POST['prod_price']
        prod_category = request.POST['prod_category']
        prod_qty = request.POST['prod_qty']
        prod_desc = request.POST['prod_desc']
        prod_img = request.FILES['prod_img']

        Product.objects.create(
            prod_name=prod_name,
            prod_price=prod_price,
            prod_category=prod_category,
            prod_qty=prod_qty,
            prod_desc=prod_desc,
            prod_img=prod_img,
        )
        return redirect('view_products')

    return render(request, 'insert.html')


def blog(request):
    redeem = Redeem.objects.first()
    pixel =Pixel.objects.all()
    context = {
        'redeem': redeem,
        'pixel': pixel,

    }
    return render(request, 'blog.html', context)


def about(request):
    apply = Apply.objects.first()
    discount = Discount.objects.all()
    feedback = Feedback.objects.first()
    events = Events.objects.all()
    cart = Cart.objects.first()
    excel = Excel.objects.first()
    section = Section.objects.first()

    context = {
        'apply': apply,
        'feedback': feedback,
        'discount': discount,
        'events': events,
        'cart': cart,
        'section': section,
        'excel': excel,
    }

    return render(request, 'about.html', context)

def contact(request):
    if request.method ==  'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contact= Contact(contact_name =name, contact_email=email, contact_phone=phone, contact_message=message)
        contact.save()
        messages.success(request, 'your message had been submitted successfully')
        return redirect('/contact/')

    return render(request, 'contact.html')

def services(request):
    special = Special.objects.first()
    employee = Employee.objects.all()
    shop = Shop.objects.first()
    comment = Comment.objects.first()
    php =Php.objects.all()
    author=Author.objects.first()
    profile=Profile.objects.all()
    context ={
        'special': special,
        'employee': employee,
        'shop': shop,
        'comment': comment,
        'php': php,
        'author': author,
        'profile': profile,
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        Services.save()

        services = Services(service_name =name, service_desc =desc)
        messages.success(request, 'your message had been submitted successfully')
        return redirect('/contact/')
    return render(request, 'services.html', context)

def customers(request):
    our =Our.objects.all()
    hours =Hours.objects.first()
    alx =Alx.objects.first()
    list_desc = List_desc.objects.all()
    list = List.objects.first()
    support =Support.objects.first()
    main = Main.objects.first()
    context ={
        'our': our,
        'hours':hours,
        'alx': alx,
        'list_desc': list_desc,
        'support': support,
        'main': main,
        'list': list,
    }
    return render(request, 'customers.html', context)

def blog_details(request):
    return render(request, 'blog-details.html')

def layout(request):
    return render(request, 'layout.html')

def insert(request):
    return render(request, 'insert.html')

def newsletter_subscription(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        return JsonResponse({'message': 'Subscription successful!'})
    return JsonResponse({'error': 'Invalid request'}, status=400)

def search_results(request):
    query = request.GET.get('q')
    result = []
    if query:
        result = Product.objects.filter(prod_name__icontains=query)
    return render(request, 'result.html', {'result': result, 'query': query})



