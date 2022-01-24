from django.shortcuts import render
from rest_framework.views import APIView
#Recursos de rest_framework
from rest_framework.response import Response
from rest_framework import status

#Importaciones de serializadores
from Register.serializers import RegistroSerializer


# Create your views here.
class UserAdd(APIView):
    def post(self,request):
        serializer = RegistroSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
