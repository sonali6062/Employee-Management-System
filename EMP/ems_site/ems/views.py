from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee

# Create your views here.
def home(request):
    employees = Employee.objects.all()
    return render(request, 'ems/home.html',{'employees':employees})
def employee_detail(request,employee_id):
    try:
        employee= Employee.objects.get(id=employee_id)
    except Employee.DoesNotExist:
        raise Http404('Employee not found')
    return render(request,'ems/employee_details.html',{'employee':employee})

   
    
    