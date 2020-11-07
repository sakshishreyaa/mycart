from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    CAT_CHOICES = (
        ('clothing', 'clothing'),
        ('accessories', 'accessories'),
        ('footwear', 'footwear')
    )
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50 ,choices=CAT_CHOICES)
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    quantity=models.IntegerField()
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")


    def __str__(self):
        return self.name

class Order(models.Model):
    user=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField( default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    item = models.ManyToManyField(Product)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")

    def __str__(self):
        return "Order Id : " + str(self.order_id)

class OrderUpdate(models.Model):
    update_id  = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.order_id) + " " + str(self.update_desc)





class CustomerProfile(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    email = models.CharField(max_length=30 ,blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    contact=models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.email


