from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=255)
    wheels = models.IntegerField()
    volume = models.IntegerField()
    color = models.CharField(max_length=255)
    seats = models.IntegerField()
    producer = models.CharField(max_length=255, default=1)
    v_or_i = models.IntegerField(max_length=255, default=1)
    sui = models.IntegerField(default=1)

    def makeSound():
        print("WROOM")
    
    def __str__(self):
        return self.name