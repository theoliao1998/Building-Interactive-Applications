from django.contrib import admin

# Register your models here.

from unesco.models import Category, States, Region, Iso, Site


admin.site.register(Category)
admin.site.register(States)
admin.site.register(Region)
admin.site.register(Iso)
admin.site.register(Site)
