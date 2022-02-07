from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import exceptions
import json
import os.path
##from pathlib import Path

#Importaciones de modelos agragados
from loadImage.models import TablaImage

#Importaciones de serializadores
from loadImage.serializers import TerceraTablaSerializer

# Create your views here.

class ImageLoad(APIView):
    ## Metodo Response_Custom
 def response_custom(self,messages,pay_load, status):
        responseOk = {"messages":messages,"pay_load":pay_load,"status":status}
        response1 = json.dumps(responseOk)
        responseOk2 = json.loads(response1)
        return responseOk2

 def get(self, request, format=None):
        queryset = TablaImage.objects.all()
        serializer = TerceraTablaSerializer(queryset, many = True, context = {'request':request})
        return Response(self.response_custom("Succes",serializer.data, status = status.HTTP_200_OK))
        
 def post(self, request):
     if 'url_img' not in request.data:
         raise exceptions.ParseError("No se selecciono ningun archivo")
     archivos =str(request.FILES)
     serializer = TerceraTablaSerializer(data=request.data)
     if serializer.is_valid():
           validated_data = serializer.validated_data
          ## print(validated_data)
           #archivo = validated_data['url_img']
           #archivo.name_img = validated_data['name_img']
           #archivo.format_img = validated_data['format_img']
           #validated_data['url_img'] = archivo
           #validated_data['name_img'] = archivo.name_img
           #validated_data['format_img'] = archivo.format_img
            # Convertir y guardar el modelo
           img = TablaImage(**validated_data)
           img.save()

           #serializer_response = TerceraTablaSerializer(img)

           return Response(self.response_custom("Succes",serializer.data, status = status.HTTP_201_CREATED))
     return Response(self.response_custom("Errors",serializer.errors,status = status.HTTP_400_BAD_REQUEST))
class ImageLoadDetail(APIView):

     def get_object(self, pk):
            try:
                return TablaImage.objects.get(pk = pk)
            except TablaImage.DoesNotExist:
                return 0

     def get(self, request, pk ,format=None):
            idResponse = self.get_object(pk)
            if idResponse != 0:
                idResponse = TerceraTablaSerializer(idResponse)
                return Response(idResponse.data, status.HTTP_200_OK)
            return Response("No hay datos", status.HTTP_400_BAD_REQUEST)      

     def put(self, request,pk, format=None):
        idResponse = self.get_object(pk)
        archivos = request.data['url_img']
        nombre, formato = os.path.splitext(archivos.name)
        request.data['name_img'] = nombre
        request.data['format_img'] = formato
        serializer = TerceraTablaSerializer(idResponse, data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas, status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

       
     def delete(self, request , pk , format=None):
             idResponse = self.get_object(pk)
             if idResponse != 0:
                 idResponse.url_img.delete(save=True)
                 idResponse.delete()
                 return Response("El dato se elimino", status= status.HTTP_201_CREATED)
             return Response("Nose encontro", status= status.HTTP_400_BAD_REQUEST)