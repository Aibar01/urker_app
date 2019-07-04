from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Employee


class EmployeeListView(ListView):
    queryset = Employee.objects.filter(is_active=True)
    template_name = 'employee/employee_list.html'
    context_object_name = 'employees'


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee/employee_detail.html'


class SearchEmployeeListView(ListView):
    template_name = 'employee/employee_list.html'
    context_object_name = 'employees'

    def get_context_data(self, *args, **kwargs):
        context = super(SearchEmployeeListView, self).get_context_data(*args, **kwargs)
        context["query"] = self.request.GET.get('q')
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q')
        if query is not None:
            lookups = Q(id__icontains=query) | Q(name__icontains=query) | Q(surname__icontains=query) | Q(position__position__icontains=query)
            return Employee.objects.filter(lookups).distinct()
        return Employee.objects.none()



