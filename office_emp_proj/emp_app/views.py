from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department
from datetime import datetime

# Create your views here.
 
def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    print(context)
    return render(request,'all_emp.html',context)


def add_emp(request):
    if request.method == 'POST':
        try:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            salary = int(request.POST['salary'])
            bonus = int(request.POST['bonus'])
            phone = int(request.POST['phone'])
            department = int(request.POST['department'])
            role = int(request.POST['role'])
            hire_date = request.POST['hire_date']

            new_emp = Employee(
                first_name=first_name,
                last_name=last_name,
                salary=salary,
                bonus=bonus,
                phone=phone,
                dept_id=department,
                role_id=role,
                hire_date=hire_date
            )
            new_emp.save()
            return HttpResponse('Employee added successfully')
        except Exception as e:
            return HttpResponse(f'An error occurred: {e}')
    elif request.method == 'GET':
        return render(request, 'add_emp.html')
    else:
        return HttpResponse('Invalid request method')

def remove_emp(request):
    return render(request,'remove_emp.html')

def filter_emp(request):
    return render(request,'filter_emp.html')
