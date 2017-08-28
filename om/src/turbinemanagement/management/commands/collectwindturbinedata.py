from django.core.management.base import BaseCommand, CommandError
from turbinemanagement.models.windturbine import WindTurbine
from appcore.models.audit_log import AuditLog
import requests

# === Command to handle data sync between Control and O&M ===

class Command(BaseCommand):
    """
    The Command class defines the commandline functionality for the data sync between O&M and the Control instances in the wind turbines
    """

    # === Main entry point for the command ===
    def handle(self, *args, **options):
        """
        Handle the execution of the command by invoking this method and synchronize the data from the windturbines into the O&M database

        :param *args: any additional positional arguments
        :param **options: any named options/keyword arguments
        """
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
                    response = requests.get('http://' + windturbine.ip_address + ':80/windturbinedata/all/')
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
                        message = "The windturbine " + str(windturbine) + " at " + windturbine.ip_address + " returned error with status " + response.status_code
                        AuditLog.objects.create(name="System", message=message)
                        print(message)
                except Exception as e:
                    message = "The data sync with windturbine " + str(windturbine) + " at " + windturbine.ip_address + " failed with the following error: " + str(e)
                    AuditLog.objects.create(name="System", message=message)
                    print(message)
