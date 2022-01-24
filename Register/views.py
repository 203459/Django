from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
#Recursos de rest_framework
from rest_framework.response import Response
from rest_framework import status

#Importaciones de serializadores
from Register.serializers import SegundaTablaSerializer

class RegisterUsers(APIView):
    def post(self, request, format=None):
        serializer = SegundaTablaSerializer(data=request.data)
       ## register = SegundaTablaSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            pw = user.password
            user.set_password(pw)
            user.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST) 
        
       