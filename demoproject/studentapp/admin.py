from django.contrib import admin

# Register your models here.
# admin.py
from .models import Faculty
from .models import Report
from .models import Payment
from .models import Student
from .models import Event
from .models import IncomeExpense

admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Report)
admin.site.register(Payment)
admin.site.register(Event)
admin.site.register(IncomeExpense)
