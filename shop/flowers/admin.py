from django.contrib import admin
from .models import Flower, FlowerTypes


# Register your models here.

admin.site.register(FlowerTypes)
admin.site.register(Flower)





