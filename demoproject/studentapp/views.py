from django.shortcuts import render
from .models import Faculty
from .models import Payment
from .models import Student
from .models import Report
from .models import Event

# Create your views here.
def index(request):
    return render(request, 'student/index.html')
def viewstudent(request):
    students = Student.objects.all()
    return render(request,'student/viewstudent.html',{'students': students})


def facultyview(request):
    faculties = Faculty.objects.all()
    return render(request,'student/facultyview.html', {'faculties': faculties})

def viewreport(request):
    reports = Report.objects.all()
    return render(request,'student/viewreport.html', {'reports': reports })


def viewevent(request):
    events = Event.objects.all()
    return render(request,'student/viewevent.html',{'events':events})
def payment(request):
    payments = Payment.objects.all()
    return render(request,'student/payment.html', {'payments': payments})