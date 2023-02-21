from django.urls import path
from . import views


app_='nameschool'
urlpatterns = [
    path('', views.home , name='home'),
    path('timetable/',views.timetable,name='timetable'),
    path('AddAttendance/',views.addattendance,name='addattendance'),   
    path('results/',views.addmarks,name='addmarks'), 
    path('AddNotice/',views.addnotice,name='addnotice'),
] 

