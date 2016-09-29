from rest_framework import serializers
from user.models import Stb, PhysicalStb

class StbSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stb
        fields = ('stb_id', 'iptv_status_code')

class PhysicalSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PhysicalStb
        fields = ('stb_id', 'mac_address')
