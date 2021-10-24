from django.db import models
from datetime import datetime

# Create your models here.
class Hiretuber(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    tuber_id = models.IntegerField()
    tuber_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self) -> str:
        return self.email

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    created_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self) -> str:
        return self.email