from django.shortcuts import render
from . models import Student
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

''' this is API tested by Browsable API which is built-in of DRF itself ok '''

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def student_api(request,pk=None):#here pk value comes from url.py
    if request.method == 'GET':
        id=pk                       
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data) #it return with json format
        else:
            stu = Student.objects.all()# if requested for all data from DB
            serializer = StudentSerializer(stu,many=True)
            return Response(serializer.data) 


    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        id = pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data deleted'})

