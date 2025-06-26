from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import Employee,Job

def home(request):
    return render(request,'home.html',{"employee":Employee.objects.all()})


def employee_detail(request,employee_id):
    return render(request,'employee_detail.html',{"employee":get_object_or_404(Employee, id=employee_id)})


