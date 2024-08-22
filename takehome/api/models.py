from django.db import models

#Main property module, allows for user input on everything except the priroities

class Property(models.Model):
    askingPrice = models.IntegerField(default=0)
    numberBeds = models.IntegerField(default=0)
    numberBaths = models.IntegerField(default=0)
    address = models.CharField(max_length=255)
    photo1 = models.CharField(max_length=255)
    photo2 = models.CharField(max_length=255)
    photo3 = models.CharField(max_length=255)
    photo1_priority = models.PositiveIntegerField(default=0)
    photo2_priority = models.PositiveIntegerField(default=1)
    photo3_priority = models.PositiveIntegerField(default=2)

    def __str__(self):
        return f"Property at {self.address}"
