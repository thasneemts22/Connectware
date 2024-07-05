
from django.urls import path,include

from studentapp import views
urlpatterns = [
    path('student',views.index,name='student'),
    path('viewstudent',views.viewstudent,name='viewstudent'),
    path('facultyview',views.facultyview,name='facultyview'),
    path('viewreport',views.viewreport,name='viewreport'),
    path('viewevent',views.viewevent,name='viewevent'),
    path('payment',views.payment,name='payment')
]