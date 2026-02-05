from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Person)
admin.site.register(models.tourk)
admin.site.register(models.Review)
admin.site.register(models.category)

