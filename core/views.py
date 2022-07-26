from django.shortcuts import render
from django.db.models import Q  
from core.utils import pagination
from core.models import Employee  
from core.serializer import EmployeeListSerializer
from rest_framework.response import Response 
from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view, parser_classes, permission_classes
from django.core.exceptions import MultipleObjectsReturned 
import requests
# Create your views here.


@api_view(["GET"])
def employee_list(request): 
    query_parameters = request.query_params
    page_size = query_parameters.get("page_size")
    page = query_parameters.get("page")
    search_query = query_parameters.get("q") 
    city_query = query_parameters.get("city")
    employee = Employee.objects.all() 
    sort_param = "employee_id"
    if search_query:
        search_query = search_query.strip()
        employee = employee.filter(first_name__icontains=search_query)   
    if city_query:
        search_query = search_query.strip()
        employee = employee.filter(first_name__icontains=city_query) 
    if sort_param:
        employee = employee.order_by(sort_param)  

    page, page_size, paginator, result_page = pagination(page, page_size, employee) 
    serializer = EmployeeListSerializer(result_page, many=True)
    return Response(
    dict(
        page=page,
        total_pages=paginator.num_pages,
        page_size=page_size,
        total_items=employee.count(),
        result=serializer.data,
    )
)


@api_view(["GET"])
def employee_count(request):
    number = Employee.objects.all().count()
    return Response(dict(result=number)) 




@api_view(["PATCH"])
def edit_employee_data(request): 
    employee_id = request.data.get("employee_id") 
    first_name = request.data.get("first_name") 
    last_name = request.data.get("last_name")  
    email = request.data.get("email")
    city = request.data.get("city")
    phone_number = request.data.get("phone_number")  
    employee = Employee.objects.filter(employee_id=employee_id).update(first_name=first_name,last_name=last_name,email=email,city=city,phone_number=phone_number)  
    return Response(
        dict(
            detail=(
                "Employee Details Updated"
            )
        )
    )
    # employee.save()

@api_view(["DELETE"])
def delete_employee(request): 
    query_parameters = request.query_params  
    employee_id = query_parameters.get("employee_id")
    try:
        employee = Employee.objects.select_for_update().get(employee_id=employee_id)
    except Employee.DoesNotExist:
        raise ValidationError(dict(detail=("Employee not found!")))

    Employee.objects.get(employee_id=employee_id).delete()   
    return Response(
        dict(
            detail=(
                "Employee is Deleted"
            )
        )
    )


@api_view(["POST"])
def add_employee(request): 
    employee_id = request.data.get("employee_id") 
    first_name = request.data.get("first_name") 
    last_name = request.data.get("last_name")  
    email = request.data.get("email")
    city = request.data.get("city")
    # phone_number = request.data.get("phone_number")     
    try:
        employee = Employee.objects.create(employee_id=employee_id,first_name=first_name,last_name=last_name,email=email,city=city)  
    except Exception as e:
        raise ValidationError(dict(detail=("Duplicate Data")))
    return Response(
        dict(
            detail=(
                "Employee Details added"
            )
        )
    )



    



