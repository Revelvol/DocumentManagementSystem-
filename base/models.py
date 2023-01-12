from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Departement(models.Model):
    name = models.CharField(max_length=200, null= True)
    class Meta:
        ordering = [
            "name",
        ]
    def __str__(self):
        return self.name
class Position(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=10000, null =True, blank= True)
    departement = models.ForeignKey(Departement, on_delete= models.CASCADE , null = True)
    #location, nanti di link ke many to one dimana dia banyak kayak adress, lantai, ruangan, dkk
    class Meta:
        ordering = [
            "name",
        ]
    def __str__(self):
        return self.name

class User(AbstractUser): #jangan lupa abstract user udh ada password as a value
    name = models.CharField (unique= True,max_length=200, null = True )
    email = models.EmailField(unique=True , null = True , blank=False)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL,null=True, blank= True )
    manager = models.ForeignKey('self', on_delete=models.SET_NULL,null=True, blank=True)
    #adrreess
    #created
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email', 'username' ] #disini bmungkin ada problem dimana username mesti unique
    class Meta:
        ordering = [
            "-name",
        ]
    def __str__(self):
        return f"{str(self.name)} |  {str(self.position)} "




