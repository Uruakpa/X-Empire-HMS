from django.db import models
from django.contrib.auth.models import User

# Create your models here.
    
class DrinkMenu(models.Model):
    menuItems = models.TextField()
    category = models.ForeignKey("DrinkCategory",on_delete=models.CASCADE, null=True)
    type = models.CharField
    price = models.IntegerField    
    
    def _str_(self):
        return str(self.menuItems) + " " + str(self.startDate)

class DrinkCategory(models.Model):
    name = models.CharField(max_length=50, null=True)
    
    
class Drinktype(models.Model):
    name = models.CharField
    type = models.ImageField( upload_to='media/Drinktype', )
    stock = models.IntegerField
    