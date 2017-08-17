from django.db import models
from .audit_log import AuditLog

class BaseModel(models.Model):

    class Meta:
        abstract = True

#    def save(self, *args, **kwargs):

#    @staticmethod
#    def create(*args, **kwargs):
#        return self.objects.create(*args, **kwargs)
#
#    @staticmethod
#    def all(*args, **kwargs):
#        return self.objects.all(*args, **kwargs)
#
#    @staticmethod
#    def find(id, *args, **kwargs):
#        return self.objects.filter(id=id, *args, **kwargs)
