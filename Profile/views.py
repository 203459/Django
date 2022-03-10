import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions
import os
#Importaciones de modelos
from Profile.models import Profile
from django.contrib.auth.models import User

#Importacion de serializers
from Profile.serializers import ProfileSerializer

# Create your views here.

class ProfileTable(APIView):
 def get_objectUser(self, idUser):
        try:
            return User.objects.get(pk = idUser)
        except User.DoesNotExist:
            return 0

 def post(self, request):
        if 'url_img' not in request.data:
            raise exceptions.ParseError(
                "No has seleccionado el archivo a subir")
        archivos = request.data['url_img']
        idUser = request.data['id_user']
        user = self.get_objectUser(idUser)
        if(user != 0):
            serializer = ProfileSerializer(data=request.data)
            if serializer.is_valid():
                validated_data = serializer.validated_data
                profile = Profile(**validated_data)
                profile.save()
                serializer_response = ProfileSerializer(profile)
                return Response(serializer_response.data, status=status.HTTP_201_CREATED)
            return Response("Metodo post no permitido", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("El usuario no existe")

class ProfileTableDetail(APIView):
    def get_object(self, pk):
        try:
            return Profile.objects.get(id_user = pk)
        except Profile.DoesNotExist:
            return 0
    
    def get(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 0:
            idResponse = ProfileSerializer(idResponse)
            return Response(idResponse.data, status = status.HTTP_200_OK)
        return Response("No hay datos", status = status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk, format=None):
        archivos = request.data['url_img']
        idResponse = self.get_object(pk)
        if(idResponse != 0):
            serializer = ProfileSerializer(idResponse)
            try:
                os.remove('assets/'+str(idResponse.url_img))
            except os.error:
                print("La imagen no existe")
            idResponse.url_img = archivos
            idResponse.save()
            return Response("Todo salio bien",status.HTTP_201_CREATED)
        else:
            return Response("halgo salio mal")
    
    def delete(self, request, pk):
        profile = self.get_object(pk)
        if profile != 0:
            profile.url_img.delete(save=True)
            return Response("Imagen eliminada",status=status.HTTP_204_NO_CONTENT)
        return Response("Imagen no encontrada",status = status.HTTP_400_BAD_REQUEST)

class UserProfileData (APIView):
    def res_custom(self, user, status):
        response = {
            "first_name" : user[0]['first_name'],
            "last_name" : user[0]['last_name'],
            "username" : user[0]['username'],
            "email" : user[0]['email'],
            "status" : status
        }
        return response
    
    def get(self, request, pk, format=None):
        user = User.objects.filter(pk=pk)
        if(user != 0):
            responseData = self.res_custom(user.values(), status.HTTP_200_OK)
            return Response(responseData)
        else:
            return Response("Este usuario no existe", status = status.HTTP_404_NOT_FOUND)
        
    
    def put(self, request, pk, format=None):
        data = request.data
        user = User.objects.filter(pk = pk)
        if(user != 404):
            user.update(username = data.get('username'))
            user.update(first_name = data.get('first_name'))
            user.update(last_name = data.get('last_name'))
            user.update(email = data.get('email'))
            return Response(self.res_custom(user.values(), status.HTTP_200_OK))
        else:
            return Response("Este usuario no existe", status = status.HTTP_400_BAD_REQUEST)