from django.contrib import admin
from .models import Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('address', 'askingPrice', 'numberBeds', 'numberBaths', 'photo1', 'photo2', 'photo3')

