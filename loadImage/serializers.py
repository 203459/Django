from rest_framework import routers, serializers, viewsets
#Importacion de modelos
from loadImage.models import TablaImage

class SegundaTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TablaImage
        fields = ('name_img','url_img','format_img')