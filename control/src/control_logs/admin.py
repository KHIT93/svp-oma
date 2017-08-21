from django.contrib import admin

# Register your models here.
from .models.control_log import ControlLog

admin.site.register(ControlLog)