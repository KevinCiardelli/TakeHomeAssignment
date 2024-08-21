from django.db import models

class Property(models.Model):
    askingPrice = models.IntegerField(default=0)
    numberBeds = models.IntegerField(default=0)
    numberBaths= models.IntegerField(default=0)
    address = models.CharField(max_length= 255)

    def __str_(self):
        return self.title