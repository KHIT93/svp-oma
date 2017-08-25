from django.db import models
from .audit_log import AuditLog

# === Base model for later use when all models are going to performn the same tasks no matter what their use case is ===

class BaseModel(models.Model):

    class Meta:
        abstract = True
