from django.urls import path
from core.views import (
    add_employee,
    edit_employee_data,
    delete_employee,
    employee_count,
    employee_list
)

urlpatterns = [ 
    path("add_employee", add_employee, name="add_employee"), 
    path("edit_employee_data", edit_employee_data, name="edit_employee_Data"), 
    path("delete_employee/", delete_employee, name="delete_employee"),
    path("employee_count", employee_count, name="employee_count"), 
    path("employee_list", employee_list, name="employee_list"),
    
]