from django.db import models

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length = 150)
    def __str__(self):
        return self.name
class Item(models.Model):
    item_name = models.CharField(max_length=100)
    under_group = models.ForeignKey('Group', on_delete=models.CASCADE)

    def __str__(self):
        return self.item_name
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    under_group = models.ForeignKey('Group', on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

class Customer(models.Model):
    customer_name = models.CharField( max_length=100)
    address = models.CharField(max_length=100)
    city = models.ForeignKey('City', on_delete=models.CASCADE)
    state = models.ForeignKey('State', on_delete=models.CASCADE)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)
    pin= models.CharField(max_length=100)
    phone1=models.IntegerField()
    phone2=models.IntegerField()
    tax = models.ForeignKey('Tax', on_delete=models.CASCADE)



    def __str__(self):
        return self.customer_name

class City(models.Model):
    city_name = models.CharField(max_length = 150)
    state=models.ForeignKey("State",  on_delete=models.CASCADE)
    def __str__(self):
        return self.city_name
class State(models.Model):
    state_name = models.CharField(max_length = 150)
    country=models.ForeignKey("Country",  on_delete=models.CASCADE)
    def __str__(self):
        return self.state_name
class Country(models.Model):
    country_name = models.CharField(max_length = 150)
    def __str__(self):
        return self.country_name
    
class Tax(models.Model):
    tax_name = models.CharField(max_length = 150)
    effective_date= models.DateField()
    rate_of_tax = models.IntegerField()
    assesseble_value= models.ForeignKey("Assessable_value", on_delete=models.CASCADE)
    def __str__(self):
        return self.tax_name
class Assessable_value(models.Model):
    value=models.CharField(max_length=100)
    def __str__(self):
        return self.value




