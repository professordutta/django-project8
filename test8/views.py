from django.shortcuts import render,HttpResponse
from .models import Mriic
from .serializers import EmpSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

def home(request):
    return HttpResponse("<h1>Hello!</h1>")


@api_view(['GET', 'POST'])
def employeeview(request):
    if request.method == 'GET':
        mriic_emp = Mriic.objects.all()
        mr_emp = EmpSerializer(mriic_emp, many = True)
        return Response(mr_emp.data)
    elif request.method == 'POST':
        serializer = EmpSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def emp_detail(request, pk):
    try:
        employee = Mriic.objects.get(pk=pk)
    except employee.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = EmpSerializer(employee)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EmpSerializer(employee, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
