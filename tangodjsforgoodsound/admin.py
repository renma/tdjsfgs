from django.contrib import admin

# Register your models here.
from .models import DJ

# Register
# admin.site.register(DJ)


# Create an admin class
class DJAdmin(admin.ModelAdmin):
    list_display = ("name", "number_of_milongas", "last_changed", "useremail", )


# Register DJ Model and DJ Admin
admin.site.register(DJ, DJAdmin)
