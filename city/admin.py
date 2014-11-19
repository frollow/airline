from django.contrib import admin
from django.contrib.admin import ModelAdmin
from city.models import City


class CityAdmin(ModelAdmin):
    model = City
    list_display = ('city', 'country')


admin.site.register(City, CityAdmin)