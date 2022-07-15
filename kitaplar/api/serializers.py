from dataclasses import fields
from rest_framework import serializers
from ..models import Kitap, Yorum


class YorumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Yorum
        exclude = ['kitap']


class Kitapserializer(serializers.ModelSerializer):
    yorumlar = YorumSerializer(many=True, read_only=True)

    class Meta:
        model = Kitap
        fields = '__all__'
