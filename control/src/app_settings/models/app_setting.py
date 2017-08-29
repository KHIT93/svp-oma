from django.db import models

class AppSetting(models.Model):
    """
    The AppSetting class is responsible for the configuration data

    Each entry includes these fields:

    :param key: A character representation for the title of the value

    :param value: A character representation that holds the value for the key
    """
    key = models.CharField(max_length=255, unique=True)
    value = models.TextField()

    def __str__(self):
        return str(self.key)

    def __unicode__(self):
        return self.__str__()