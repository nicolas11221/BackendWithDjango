from rest_framework import serializers
from .models import Chela


class ChelaSerializers(serializers.ModelSerializer):
    class Meta:
        #Traigo todos los campos con __all__
        model = Chelafields = '__all__'