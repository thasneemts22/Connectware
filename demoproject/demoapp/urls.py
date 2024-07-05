
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static
from demoapp import views
urlpatterns = [
    path('',views.index,name='index'),
    path('event',views.event,name='event'),
    path('registration',views.registration,name='registration'),
    path('login',views.loginview,name='login')

]
