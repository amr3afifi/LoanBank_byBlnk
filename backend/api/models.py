from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import json
from django.utils.timezone import now

    
    
class User(models.Model):
    PROVIDER = 'provider'
    CUSTOMER = 'customer'
    BANK = 'bank'

    STATUS_CHOICES = (
        (PROVIDER, 'Provider'),
        (CUSTOMER, 'Customer'),
        (BANK, 'Bank')
    )
    
    username = models.CharField(max_length=50,unique=True,blank=False)
    password = models.CharField(max_length=300,blank=False)
    type = models.CharField(max_length=10, choices=STATUS_CHOICES, default=CUSTOMER)
    
    def __str__(self):
        return self.username + ' ' + self.type
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,sort_keys=True, indent=4)
    
class LoanTermCustomer(models.Model):
    name = models.CharField(max_length=50,unique=True,blank=False)
    min= models.PositiveIntegerField(blank=False, validators=[MinValueValidator(1)])
    max= models.PositiveIntegerField(blank=False, validators=[MinValueValidator(1)])
    duration= models.PositiveIntegerField(blank=False, validators=[MinValueValidator(1),MaxValueValidator(120)])
    interest= models.FloatField(blank=False, validators=[MinValueValidator(0),MaxValueValidator(100)])
    
class LoanCustomer(models.Model):
    name = models.CharField(max_length=50,blank=False)
    value= models.PositiveIntegerField(blank=False, validators=[MinValueValidator(1)])
    paid= models.PositiveIntegerField(default=0)
    accepted=models.BooleanField(default=False)
    start_date=models.DateTimeField(default=now, blank=True)
    term_id=models.PositiveIntegerField(blank=False)
    user_id=models.PositiveIntegerField(blank=False)
    
class LoanTermProvider(models.Model):
    name = models.CharField(max_length=50,unique=True,blank=False)
    min= models.PositiveIntegerField(blank=False, validators=[MinValueValidator(1)])
    max= models.PositiveIntegerField(blank=False, validators=[MinValueValidator(1)])
    duration= models.PositiveIntegerField(blank=False, validators=[MinValueValidator(1),MaxValueValidator(120)])
    interest= models.FloatField(blank=False, validators=[MinValueValidator(0),MaxValueValidator(100)])
    
class LoanProvider(models.Model):
    name = models.CharField(max_length=50,blank=False)
    value= models.PositiveIntegerField(blank=False, validators=[MinValueValidator(1)])
    paid= models.PositiveIntegerField(default=0)
    accepted=models.BooleanField(default=False)
    start_date=models.DateTimeField(default=now, blank=True)
    term_id=models.PositiveIntegerField(blank=False)
    user_id=models.PositiveIntegerField(blank=False)