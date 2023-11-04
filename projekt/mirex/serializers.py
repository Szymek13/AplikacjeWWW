from rest_framework import serializers
from .models import Osoba, Stanowisko

class OsobaSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    imie = serializers.CharField(required=True)
    nazwisko = serializers.CharField(required=True)
    stanowisko = serializers.PrimaryKeyRelatedField(queryset=Stanowisko.objects.all())

    def create(self, validated_data):
        return Osoba.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('imie', instance.name)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.stanowisko = validated_data.get('stanowisko', instance.stanowisko)
        instance.save()
        return instance

class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stanowisko
        fields = ['nazwa', 'opis']
        read_only_fields = ['nazwa']