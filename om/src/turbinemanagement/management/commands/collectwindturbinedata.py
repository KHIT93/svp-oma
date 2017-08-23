from django.core.management.base import BaseCommand, CommandError
from turbinemanagement.models.windturbine import WindTurbine
from appcore.models.audit_log import AuditLog
import requests

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Starting data sync from windturbines")
        for windturbine in WindTurbine.objects.all():
            if windturbine.ip_address == "0.0.0.0":
                logmessage = "Windturbine " + str(windturbine) + " skipped due to missing IP-address"
                AuditLog.objects.create(name="System", message=logmessage)
                print(logmessage)
            else:
                logmessage = "Running data sync for windturbine " + str(windturbine) + " at " + windturbine.ip_address
                AuditLog.objects.create(name="System", message=logmessage)
                print(logmessage)
                try:
                    response = requests.get('http://' + windturbine.ip_address + ':8000/windturbinedata/all/')
                    if response.status_code == 200:
                        serializer = WindturbineDataSerializer(data=response.json(), many=True)
                        if serializer.is_valid():
                            serializer.save()
                            message = "Windturbine data for windturbine " + str(windturbine) + " at " + windturbine.ip_address + " has been updated"
                            AuditLog.objects.create(name="System", message=message, api_response=response.json())
                            print(message)
                        else:
                            message = "The data recieved from windturbine " + str(windturbine) + " at " + windturbine.ip_address + " returned invalid data. The response data has been saved to the audit log for troubleshotting purposes"
                            AuditLog.objects.create(name="System", message=message, api_response=response.json())
                            print(message)

                    else:
                        message = "The windturbine " + str(windturbine) + " at " + windturbine.ip_address + " returned error with status " + r.status_code
                        AuditLog.objects.create(name="System", message=message)
                        print(message)
                except:
                    message = "The windturbine " + str(windturbine) + " at " + windturbine.ip_address + " could not be reached"
                    AuditLog.objects.create(name="System", message=message)
                    print(message)
