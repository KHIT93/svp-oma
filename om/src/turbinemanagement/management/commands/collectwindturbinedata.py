from django.core.management.base import BaseCommand, CommandError
from turbinemanagement.models.windturbine import WindTurbine
import requests

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting data sync from windturbines")
        for windturbine in WindTurbine.objects.all():
            if windturbine.ip_address == "0.0.0.0":
                print("Windturbine " + windturbine + " skipped due to missing IP-address")
            else:
                print("Running data sync for windturbine " + windturbine + " at " + windturbine.ip_address)
                try:
                    r = requests.get('http://' + windturbine.ip_address + '/windturbinedata/all/')
                    if r.status_code == 200:
                        print(r)
                except:
                    print("The windturbine " + windturbine + " at " + windturbine.ip_address + " could not be reached")
