from django.shortcuts import render, redirect
from django.views import View
from .models import Employee
from .forms import EmployeeForm


class EmployeeListView(View):
    def get(self, request):
        employees = Employee.objects.all()
        return render(request, 'employees/employee_list.html', {'employees': employees})


class EmployeeCreateView(View):
    def get(self, request):
        form = EmployeeForm()
        return render(request, 'employees/employee_form.html', {'form': form})

    def post(self, request):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
        return render(request, 'employees/employee_form.html', {'form': form})


class EmployeeUpdateView(View):
    def get(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        form = EmployeeForm(instance=employee)
        return render(request, 'employees/employee_form.html', {'form': form})

    def post(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
        return render(request, 'employees/employee_form.html', {'form': form})


class EmployeeDeleteView(View):
    def get(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        return render(request, 'employees/employee_confirm_delete.html', {'employee': employee})

    def post(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        employee.delete()
        return redirect('employee_list')


class EmployeeDetailView(View):
    def get(self, request, pk):
        employee = Employee.objects.get(pk=pk)
        return render(request, 'employees/employee_detail.html', {'employee': employee})


class EmployeeSearchView(View):
    def get(self, request):
        query = request.GET.get('q')
        employees = []

        if query:
            employees = Employee.objects.filter(first_name__icontains=query)

        return render(request, 'employees/employee_search.html', {'employees': employees, 'query': query})
