from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def home(request):

    snotice=notice.objects.all()
    sattendance=attendance.objects.all()
    smarks=marks.objects.all()

    context={
        'notice':snotice,
        'marks':smarks,
        'attendance':sattendance,
    }
    return render(request,'school/home.html',context)


def addattendance(request):
    if request.user.is_authenticated:
        form=addattendanceform()
        if request.method=='POST':
            form=addattendanceform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'school/AddAttendance.html',context)
    else:
        return redirect('home')

def addmarks(request): 
    if request.user.is_authenticated:
        form=addmarksform()
        if(request.method=='POST'):
            form=addmarksform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'school/results.html',context)
    else: 
        return redirect('home')  
 
def addnotice(request):    
    if request.user.is_authenticated:
        form=addnoticeform()
        if(request.method=='POST'):
            form=addnoticeform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'school/AddNotice.html',context)
    else: 
        return redirect('home') 

def timetable(request):

    return render(request,'school/timetable.html',{})


