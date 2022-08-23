from django.contrib import admin

from .models import Flight, Airport, Passanger
# Register your models here.
class passangerAdmin(admin.ModelAdmin):
     filter_horizontal = ("flights",)
     list_display = ("first","last","id")

class airportAdmin(admin.ModelAdmin):
     list_display = ("city","code")


admin.site.register(Flight)
admin.site.register(Airport, airportAdmin)
admin.site.register(Passanger,passangerAdmin)