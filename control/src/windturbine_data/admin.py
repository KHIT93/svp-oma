from django.contrib import admin

# Register your models here.
from .models.windturbine_data import WindturbineData

admin.site.register(WindturbineData)