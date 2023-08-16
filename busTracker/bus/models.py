from django.db import models

class Bus(models.Model):
    plate = models.CharField(max_length=6)
    routeName = models.CharField(max_length=255)
    def __str__(self):
        return self.plate +' - '+self.routeName