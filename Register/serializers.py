from dataclasses import field, fields
from rest_framework import routers, serializers, viewsets

#Importacion de modelos
from django.contrib.auth.models import User

class SegundaTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','password')