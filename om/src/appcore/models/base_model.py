from django.db import models
from .audit_log import AuditLog

class BaseModel(models.Model):

    class Meta:
        abstract = True

#    def save(self, *args, **kwargs):

    @staticmethod
    def create(self, *args, **kwargs):
        return self.objects.create(*args, **kwargs)

    @staticmethod
    def all(self, *args, **kwargs):
        return self.objects.all(*args, **kwargs)

    @staticmethod
    def find(self, id, *args, **kwargs):
        return self.objects.filter(id=id, *args, **kwargs)
