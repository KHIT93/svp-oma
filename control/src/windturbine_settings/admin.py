from django.contrib import admin

# Register your models here.
from .models.windturbine_setting import WindturbineSetting

admin.site.register(WindturbineSetting)