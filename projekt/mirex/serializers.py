from rest_framework import serializers
from .models import Osoba, Stanowisko
from datetime import date

class OsobaSerializer(serializers.ModelSerializer):

    def validate_imie(self, value):
        if not value.isalpha():
            raise serializers.ValidationError(
                "Imię musi składać się tylko z liter!"
            )
        return value

    def validate_data_dodania(self, value):
        if value > date.today():
            raise serializers.ValidationError(
                "Data dodania nie może być z przyszłości"
            )

    id = serializers.IntegerField(read_only=True)
    imie = serializers.CharField(required=True, validators=[validate_imie])
    nazwisko = serializers.CharField(required=True)
    plec = serializers.IntegerField(required=True)
    stanowisko = serializers.PrimaryKeyRelatedField(queryset=Stanowisko.objects.all())
    data_dodania = serializers.DateField(required=True)

    def create(self, validated_data):
        return Osoba.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('imie', instance.name)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.plec = validated_data.get('plec', instance.plec)
        instance.stanowisko = validated_data.get('stanowisko', instance.stanowisko)
        instance.save()
        return instance

    class Meta:
        model = Osoba
        read_only_fields = ['id']
        fields = ['id', 'data_dodania', 'nazwa', 'plec', 'stanowisko']

class StanowiskoSerializer(serializers.ModelSerializer):
    nazwa = serializers.CharField(required=True)
    opis = serializers.CharField(required=True)

    def create(self, validated_data):
        return Stanowisko.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.opis = validated_data.get('opis', instance.opis)
        instance.save()
        return instance

    class Meta:
        model = Stanowisko
        read_only_fields = ['id']
        fields = ['id', 'nazwa', 'opis']