from django.db import models
from django.contrib.auth.models import  User


# Create your models here.


class Category_BOOK(models.TextChoices):
    ACTION = 'ACTION',
    HOME  = 'HOME',
    PYTHON = 'PYTHON',
    PHP  =  'PHP',
    JAVA =  'JAVA'
    



class Book (models.Model):
    name         = models.CharField(max_length=50   , verbose_name="Name")
    price        = models.DecimalField(max_digits=7, decimal_places=2 , default=0  , verbose_name="Price")
    category     =  models.CharField( max_length=50  , choices=Category_BOOK.choices , verbose_name="Category")
    description  =   models.TextField(verbose_name="Description")
    stock        = models.IntegerField(default=0  ,verbose_name="Stock")
    cost         = models.DecimalField(max_digits=7, decimal_places=2 , default=0  , verbose_name="Cost")
    create_At    =  models.DateTimeField( auto_now=False, auto_now_add=True ,verbose_name="Create AT") 
    user         = models.ForeignKey(User, verbose_name="User" , null=True, on_delete=models.SET_NULL)
    
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
    
    def __str__(self):
        return self.name
    
    
# class ReView(models.Model):
#     book  = models.ForeignKey("Book", verbose_name=("ReView"), on_delete=models.CASCADE)
#     def __str__(self):
#         pass

#     class Meta:

#         verbose_name = 'ReView'
#         verbose_name_plural = 'ReViews'
    
    