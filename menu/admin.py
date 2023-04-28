from django.contrib import admin
from .models import Menu0, Menu1, Menu2, Menu3, Menu4

class Menu0Admin(admin.ModelAdmin):
    list_display = ("id", "name")

class Menu1Admin(admin.ModelAdmin):
    list_display = ("id", "name", "previous")

# Register your models here.
admin.site.register(Menu0, Menu0Admin)
admin.site.register(Menu1, Menu1Admin)
admin.site.register(Menu2)
admin.site.register(Menu3)
admin.site.register(Menu4)