from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Equipment)
admin.site.register(models.Component)
admin.site.register(models.Sensor)