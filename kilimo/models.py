from django.db import models

# Customer Model
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField()
    registered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Product Model
class Product(models.Model):
    prod_name = models.CharField(max_length=100)
    prod_price = models.IntegerField()
    prod_category = models.CharField(max_length=50)
    prod_qty = models.IntegerField()
    prod_img = models.ImageField(upload_to='products/', blank=True, null=True)
    prod_desc = models.TextField()


    def __str__(self):
        return self.prod_name

# Order Model
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')],
        default='Pending'
    )

    def __str__(self):
        return f"Order {self.id} by {self.customer.name}"

# Pricing Model
class Pricing(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    tier_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tier_name} - {self.product.prod_name}"

# Slider Model
class Slider(models.Model):
    slider_title = models.CharField(max_length=100)
    slider_desc = models.TextField()
    slider_image = models.ImageField(upload_to='sliders/', blank=True, null=True)

    def __str__(self):
        return self.slider_title

class Services(models.Model):
    service_name = models.CharField(max_length=100)
    service_desc = models.TextField()

    def __str__(self):
        return self.service_name


class Details(models.Model):
    detail_title = models.CharField(max_length=100)
    detail_desc = models.TextField()
    detail_num = models.IntegerField()
    detail_image = models.ImageField(upload_to='details/', default='default_image.jpg')

    def __str__(self):
        return self.detail_title

class Recent(models.Model):
    recent_title = models.CharField(max_length=100)
    recent_desc = models.TextField()

    def __str__(self):
        return self.recent_title

class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_image = models.ImageField(upload_to='posts/', default='default_image.jpg')
    post_group = models.CharField(max_length=100)
    post_head = models.CharField(max_length=100)

    def __str__(self):
        return self.post_title

class Testimonials(models.Model):
    testimonial_title = models.CharField(max_length=100)
    testimonial_desc = models.TextField()

    def __str__(self):
        return self.testimonial_title

class Test(models.Model):
    test_title = models.CharField(max_length=100, unique=True)
    test_desc = models.TextField()
    test_image = models.ImageField(upload_to='tests/', default='default_image.jpg')

    def __str__(self):
        return self.test_title

from django.db import models

class Json(models.Model):
    json_title = models.CharField(max_length=100, default='image')
    json_desc = models.TextField(default='text.')

    def __str__(self):
        return self.json_title

class Icon(models.Model):
    icon_title = models.CharField(max_length=100)
    icon_desc = models.TextField()

    def __str__(self):
        return self.icon_title

class Moon(models.Model):
    moon_title = models.CharField(max_length=100)
    moon_head = models.CharField(max_length=100)

    def __str__(self):
        return self.moon_title


class About(models.Model):
    about_title = models.CharField(max_length=100)
    about_head =  models.CharField(max_length=100)
    about_desc = models.TextField()
    about_image = models.ImageField(upload_to='about/', default='default_image.jpg')

    def __str__(self):
        return self.about_title

class New(models.Model):
    new_head = models.CharField(max_length=100)
    new_desc = models.TextField()

    def __str__(self):
        return self.new_head

#ABOUT SECTION.

class Section(models.Model):
    section_title = models.CharField(max_length=100)
    section_desc = models.TextField()

    def __str__(self):
        return self.section_title

class Excel(models.Model):
    excel_title = models.CharField(max_length=100)
    excel_desc = models.TextField()
    excel_button = models.CharField(max_length=100)

    def __str__(self):
        return self.excel_title

class Cart(models.Model):
    cart_title = models.CharField(max_length=100)
    cart_head = models.CharField(max_length=100)

    def __str__(self):
        return self.cart_title

class Events(models.Model):
    event_title = models.CharField(max_length=100)
    event_head = models.CharField(max_length=100)
    event_image = models.ImageField(upload_to='events/', default='default_image.jpg')

    def __str__(self):
        return self.event_title

class Feedback(models.Model):
    feedback_title = models.CharField(max_length=100)
    feedback_desc = models.TextField()

    def __str__(self):
        return self.feedback_title

class Discount(models.Model):
    discount_title = models.CharField(max_length=100)
    discount_desc = models.TextField()
    discount_number = models.IntegerField()
    discount_image = models.ImageField(upload_to='discounts/', default='default_image.jpg')

    def __str__(self):
        return self.discount_title


class Author(models.Model):
    author_title = models.CharField(max_length=100)
    author_desc = models.TextField()

    def __str__(self):
        return self.author_title

class Profile(models.Model):
    profile_title = models.CharField(max_length=100)
    profile_desc = models.TextField()
    profile_image = models.ImageField(upload_to='profiles/', default='default_image.jpg')
    profile_number = models.IntegerField()

    def __str__(self):
        return self.profile_title


class Main(models.Model):
    main_title = models.CharField(max_length=100)
    main_desc = models.TextField()

    def __str__(self):
        return self.main_title

class Support(models.Model):
    support_title = models.CharField(max_length=100)
    support_desc = models.TextField()

    def __str__(self):
        return self.support_title

class List(models.Model):
    list_title = models.CharField(max_length=100)

    def __str__(self):
        return self.list_title

class List_desc(models.Model):
    list_desc = models.TextField()

    def __str__(self):
        return self.list_desc

class Pixel(models.Model):
    pixel_title = models.CharField(max_length=100)
    pixel_desc = models.TextField()
    pixel_image = models.ImageField(upload_to='pixels/', default='default_image.jpg')

    def __str__(self):
        return self.pixel_title

class Php(models.Model):
    php_title =models.CharField(max_length=100, default='null')
    php_desc  = models.TextField(default ='null')

    def __str__(self):
        return self.php_title


class Comment(models.Model):
    comment_title = models.CharField(max_length=100)
    comment_desc = models.TextField()
    comment_image = models.ImageField(upload_to='comments/', default='default_image.jpg')
    comment_head = models.CharField(max_length=100)

    def __str__(self):
        return self.comment_title

class Shop(models.Model):
    shop_title = models.CharField(max_length=100)
    shop_head = models.CharField(max_length=100, default="Default Head")

    def __str__(self):
        return self.shop_title

class Employee(models.Model):
    employee_title = models.CharField(max_length=100)
    employee_desc = models.TextField()
    employee_image = models.ImageField(upload_to='employees/', default='default_image.jpg')

    def __str__(self):
        return self.employee_title

class Update(models.Model):
    update_title = models.CharField(max_length=100)
    update_head = models.CharField(max_length=100)

    def __str__(self):
        return self.update_title

class Apply(models.Model):
    apply_title = models.CharField(max_length=100)
    apply_head = models.CharField(max_length=100)

    def __str__(self):
        return self.apply_title

class Special(models.Model):
    special_title = models.CharField(max_length=100)
    special_head = models.CharField(max_length=100)

    def __str__(self):
        return self.special_title

class Alx(models.Model):
    alx_title = models.CharField(max_length=100)
    alx_head = models.CharField(max_length=100)

    def __str__(self):
        return self.alx_title

class Redeem(models.Model):
    redeem_title = models.CharField(max_length=100)
    redeem_head = models.CharField(max_length=100)


    def __str__(self):
        return self.redeem_title

class User(models.Model):
    user_title = models.CharField(max_length=100)
    user_head = models.CharField(max_length=100)

    def __str__(self):
        return self.user_title

class Task(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

def __str__(self):
    return self.title















     







