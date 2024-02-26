from django.db import models

class nbaPlayer(models.Model):
    name = models.CharField(max_length=255)
    agilityScore = models.IntegerField()
    nationality = models.CharField(max_length=255, default=1)

    def makeSound():
        print("THREE POINT!!!")
    
    def __str__(self):
        return self.name