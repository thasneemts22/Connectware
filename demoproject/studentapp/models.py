from django.db import models

# Create your models here.
# models.py
# models.py
# students/models.py


class Student(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    address = models.TextField()
    duration = models.IntegerField()  # Assuming duration is in months
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name


class Faculty(models.Model):
    facultyid = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    department = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name 
    



class Report(models.Model):
    program_title = models.CharField(max_length=200)
    program_date = models.DateField()
    prepared_by = models.CharField(max_length=100)
    summary = models.TextField()
    additional_comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.program_title
    
    # models.py


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('paypal', 'PayPal'),
        # Add other payment methods as needed
    ]

    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.payment_method} - {self.amount} - {self.payment_date}"
    
class Event(models.Model):
    event_name = models.CharField(max_length=255)
    event_date = models.DateField()
    chief_guest = models.CharField(max_length=255)
    objective = models.TextField()
    venue = models.CharField(max_length=255)
    audience = models.CharField(max_length=255)

    def _str_(self):
        return self.event_name
    
    # models.py

from django.db import models

class IncomeExpense(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    receipt_no = models.CharField(max_length=20, unique=True)
    particulars = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
    date = models.DateField()

    def __str__(self):
        return f"{self.receipt_no} - {self.particulars}"




