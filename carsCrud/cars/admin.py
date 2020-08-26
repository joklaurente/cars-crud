from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'color', 'order', 'created_at')

admin.site.register(Car, CarAdmin)
