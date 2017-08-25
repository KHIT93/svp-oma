from django.db import models

class ErrorCode(models.Model):
    code = models.IntegerField()
    message = models.CharField(max_length=255)
    severity = models.IntegerField()
