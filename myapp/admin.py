from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Group)
admin.site.register(Item)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(City)
admin.site.register(State)
admin.site.register(Country )
admin.site.register(Tax)
admin.site.register(Assessable_value)

