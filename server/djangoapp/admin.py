from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class

# CarModelAdmin class

# CarMakeAdmin class with CarModelInline
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1


class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'make', 'year')
    list_filter = ('make', 'year')
    search_fields = ('name', 'make__name')


# Register models here
admin.site.register(CarMake)
admin.site.register(CarModel)
