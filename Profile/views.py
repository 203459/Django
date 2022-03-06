from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#from rest_framework import exceptions
import os
#Importaciones de modelos
from Profile.models import Profile
from django.contrib.auth.models import User

#Importacion de serializers
from Profile.serializers import ProfileSerializers

# Create your views here.

class ProfileTable(APIView):

    def get_objectUser(self, idUser):
        try:
            return User.objects.get(pk = idUser)
        except User.DoesNotExist:
            return 404
    
class ProfileTableDetail(APIView):
    def get_object(self, pk):
        try:
            return Profile.objects.get(id_user = pk)
        except Profile.DoesNotExist:
            return 404
    
    def get(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 404:
            idResponse = ProfileSerializers(idResponse)
            return Response(idResponse.data, status = status.HTTP_200_OK)
        return Response("Sin datos", status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        # idUser = request.data['id_user']
        profile = self.get_object(pk)
        if profile != 404:
            profile.url_img.delete(save=True)
            # profile.delete(save=True)
            return Response("Se elimino la imagen",status=status.HTTP_204_NO_CONTENT)
        return Response("No se encontro la imagen",status = status.HTTP_400_BAD_REQUEST)