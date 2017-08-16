from django.contrib import admin

# Register your models here.
from .models.windfarm import WindFarm
from .models.windturbine import WindTurbine
from .models.windturbine_data import WindTurbineData
from .models.windturbine_error import WindTurbineError
from .models.windturbine_setting import WindTurbineSetting

admin.site.register(WindFarm)
admin.site.register(WindTurbine)
admin.site.register(WindTurbineData)
admin.site.register(WindTurbineError)
admin.site.register(WindTurbineSetting)
