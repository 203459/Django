from dataclasses import field, fields
from pyexpat import model
from rest_framework import routers, serializers, viewsets

#Importacion de modelosq
from primerComponente.models import PrimerTabla

class PrimerTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimerTabla
        fields = ("nombre","edad")