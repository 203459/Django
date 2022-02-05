from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

#Importaciones de modelos agragados
from primerComponente.models import PrimerTabla

#Importaciones de serializadores
from primerComponente.serializers import PrimerTablaSerializer
#Importacion de tipos JSON
import json

# Create your views here.
##responseOk=  '{"message":"success","pay_load":"serializer.data","status":"status"}'
##responseOk = json.loads(responseOk)


class PrimerTablaList(APIView):
    ## Metodo Response_Custom
    def response_custom(self,messages,pay_load, status):
        responseOk = {"messages":messages,"pay_load":pay_load,"status":status}
        response1 = json.dumps(responseOk)
        responseOk2 = json.loads(response1)
        return responseOk2

    def get(self,request,format=None):
        queryset = PrimerTabla.objects.all()
        serializer = PrimerTablaSerializer(queryset,many=True,context={'request':request})
        return Response(self.response_custom("Succes",serializer.data, status = status.HTTP_200_OK))

    def post(self,request,format=None):
            serializer = PrimerTablaSerializer(data = request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(self.response_custom("Succes",datas, status = status.HTTP_201_CREATED))
            return Response(self.response_custom("Errors",serializer.errors,status = status.HTTP_400_BAD_REQUEST))

class PrimerTablaDetail(APIView):
        def get_object(self, pk):
            try:
                return PrimerTabla.objects.get(pk = pk)
            except PrimerTabla.DoesNotExist:
                return 0
        def get(self, request , pk ,format=None):
            idResponse = self.get_object(pk)
            if idResponse != 0:
                idResponse = PrimerTablaSerializer(idResponse)
                return Response(idResponse.data, status.HTTP_200_OK)
            return Response("No hay datos", status.HTTP_400_BAD_REQUEST)

        def put(self, request , pk ,format=None):
            idResponse = self.get_object(pk)
            serializer = PrimerTablaSerializer(idResponse, data= request.data)   
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data
                return Response(datas, status = status.HTTP_201_CREATED)
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

        def delete(self, request , pk , format=None):
             idResponse = self.get_object(pk)
             if idResponse != "El dato no exite":
                 idResponse.delete()
                 return Response("El dato se elimino", status= status.HTTP_201_CREATED)
             return Response("Nose encontro", status= status.HTTP_400_BAD_REQUEST)