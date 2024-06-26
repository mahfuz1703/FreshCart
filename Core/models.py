from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from authentication.models import User

# Create your models here.
STATUS_CHOICE = (
    ('process', 'Processing'),
    ('shipped', 'Shipped'),
    ('delivered', 'Delivered'),
)

STATUS = (
    ('draft', 'Draft'),
    ('disabled', 'Disabled'),
    ('rejected', 'Rejected'),
    ('in_review', 'In Review'),
    ('published', 'Published'),
)

RATING = (
    ('1', '★☆☆☆☆'),
    ('2', '★★☆☆☆'),
    ('3', '★★★☆☆'),
    ('4', '★★★★☆'),
    ('5', '★★★★★'),
)

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Category(models.Model):
    category_id = ShortUUIDField(unique=True, length=10, max_length=30, prefix="cat", alphabet="abcdefgh12345")
    title = models.CharField(max_length=150, default="Category Title")
    image = models.ImageField(upload_to="category", default="category.png")

    class Meta:
        verbose_name_plural = "Categories"

    def catefory_image(self):
        return mark_safe('<img src="%s" width="50" heignt="50 />' % (self.image.url))
    
    def __str__(self):
        return self.title
    

class Vendor(models.Model):
    vendor_id = ShortUUIDField(unique=True, length=10, max_length=30, prefix="ven", alphabet="abcdefgh12345")
    
    title = models.CharField(max_length=150, default="Vendor Title")
    image = models.ImageField(upload_to=user_directory_path, default="vendor.png")
    description = models.TextField(null=True, blank=True, default="Vendor Description")

    address = models.TextField(max_length=100, default="123 Main Street")
    contact = models.TextField(max_length=100, default="+123 (456) 6789")
    chat_response_time = models.TextField(max_length=100, default="100")
    shiping_on_time = models.TextField(max_length=100, default="100")
    authentic_rating = models.TextField(max_length=100, default="100")
    days_return = models.TextField(max_length=100, default="100")
    warenty_period = models.TextField(max_length=100, default="100")

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural = "Vendors"

    def vendor_image(self):
        return mark_safe('<img src="%s" width="50" heignt="50 />' % (self.image.url))
    
    def __str__(self):
        return self.title
    

class Tags(models.Model):
    pass

class Product(models.Model):
    product_id = ShortUUIDField(unique=True, length=10, max_length=30, prefix="pro", alphabet="abcdefgh12345")
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    
    title = models.CharField(max_length=150, default="Product Title")
    image = models.ImageField(upload_to=user_directory_path, default="product.png")
    description = models.TextField(null=True, blank=True, default="Product Description")

    price = models.DecimalField(max_digits=99999999, decimal_places=2, default=1.99)
    old_price = models.DecimalField(max_digits=99999999, decimal_places=2, default=2.99)

    specification = models.TextField(blank=True, null=True)
    # tags = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True)
    product_status = models.CharField(choices=STATUS, max_length=20, default="In Review")
    
    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=True)
    digital = models.BooleanField(default=True)

    sku = ShortUUIDField(unique=True, length=4, max_length=10, prefix="sku", alphabet="1234567890")

    date = models.DateField(auto_now_add=True)
    update = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Products"

    def product_image(self):
        return mark_safe('<img src="%s" width="50" heignt="50 />' % (self.image.url))
    
    def __str__(self):
        return self.title
    
    def get_percentage(self):
        new_price = (self.price / self.old_price) * 100
        return new_price
    

class ProductImages(models.Model):
    image = models.ImageField(upload_to="product_image", default="product.png")
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Products Images"


class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=99999999, decimal_places=2, default=1.99)
    paid_status = models.BooleanField(default=False)
    order_date = models.DateField(auto_now_add=True)
    product_status = models.CharField(choices=STATUS_CHOICE, max_length=20, default="Processing")
    
    class Meta:
        verbose_name_plural = "Cart Order"
    

class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=200)
    product_status = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=99999999, decimal_places=2, default=1.99)
    total = models.DecimalField(max_digits=99999999, decimal_places=2, default=1.99)

    class Meta:
        verbose_name_plural = "Cart Order Item"

    def order_image(self):
        return mark_safe('<img src="/media/%s" width="50" heignt="50 />' % (self.image))
    

class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Reviews"
    
    def __str__(self):
        return self.product.title
    
    def get_rating(self):
        return self.rating
    

class wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Wishlists"
    
    def __str__(self):
        return self.product.title
    

class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=150, null=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Address"