from django.db import models
from django.contrib.auth.models import User 
from django.utils.html import mark_safe
import datetime
# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField (max_length=50)
    phone = models.CharField(max_length=10)
    email=models.EmailField()
    password = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural='1. Customers'

    #to save the data
    def register(self):
        self.save()


    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email= email)
        except:
            return False


    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False

class Category(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        verbose_name_plural='2. Categories'
  
    @staticmethod
    def get_all_categories():
        return Category.objects.all()
  
    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField(max_length=600)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='uploads/products/')
    
    class Meta:
        verbose_name_plural='3. Produits'

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids)
  
    @staticmethod
    def get_all_products():
        return Products.objects.all()
  
    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter(category=category_id)
        else:
            return Products.get_all_products()

''''
class Order(models.Model):
    product = models.ForeignKey(Products,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE) #caisier pour le cas de pompe funebre
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    Client = models.CharField (max_length=50, default='', blank=True)
    phone = models.CharField (max_length=50, default='', blank=True)
    dateCeremony = models.DateField(null=True) #expiration_date
    morge= models.CharField (max_length=50, default='', blank=True)
    status = models.BooleanField (default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')
  '''




#order Items
class Orders(models.Model):
    product = models.ForeignKey(Products,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    # invoice_no=models.CharField(max_length=150)
    feu=models.CharField(max_length=150)
    ne=models.DateField(null=True)
    decede=models.DateField(null=True)
    dateCeremony = models.DateField(null=True)
    name=models.CharField(max_length=150)
    image=models.CharField(max_length=150)
    quantity=models.IntegerField()
    price=models.FloatField()
    #total=models.FloatField()
    morgue= models.CharField (max_length=50, default='', blank=True)
    avance = models.FloatField()
    #total_rest = models.FloatField()
    paid_status = models.BooleanField(default=False)
    
    def placeOrder(self):
        self.save()

    class Meta:
        verbose_name_plural='4. Les Commandes'
    def image_tag(self):
        return mark_safe('<img src="/uploads/products/%s" width="50" height="50" />' % (self.image))
    
    


    '''
    def __str__(self):
        return self.product
    def __str__(self):
        return self.customer
    def __str__(self):
        return self.avance

    '''


