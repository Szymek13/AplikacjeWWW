from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Osoba, Stanowisko
from .serializers import OsobaSerializer, StanowiskoSerializer
from django.core.exceptions import PermissionDenied

@api_view(['GET'])
def osoba_list(request):
    if request.user.has_perm('mirex.can_view_other_persons'):
        if request.method == 'GET':
            osoby = Osoba.objects.all()
            serializer = OsobaSerializer(osoby, many=True)
            return Response(serializer.data)
    if request.method == 'GET':
        osoby = Osoba.objects.filter(wlasciciel=request.user)
        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def stanowisko_list(request):
    if request.method == 'GET':
        stanowiska = Stanowisko.objects.all()
        serializer = StanowiskoSerializer(stanowiska, many=True)
        return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def osoba_detail(request, pk):
    if not request.user.has_perm('mirex.view_osoba'):
        raise PermissionDenied()
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        osoba = Osoba.objects.get(pk=pk)
        serializer = OsobaSerializer(osoba)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = OsobaSerializer(osoba, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def stanowisko_detail(request, pk):
    try:
        stanowisko = Stanowisko.objects.get(pk=pk)
    except Stanowisko.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StanowiskoSerializer(stanowisko)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = StanowiskoSerializer(stanowisko, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        stanowisko.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def osoba_add(request):
    if request.method == 'POST':
        serializer = OsobaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def osoba_list_with_string(request, search_string):
    if request.method == 'GET':
        osoby = Osoba.objects.filter(nazwa_contains=search_string)
        serializer = OsobaSerializer(osoby, many=True)
        return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
@authentication_classes([SessionAuthentication,BasicAuthentication])
@permission_classes([IsAuthenticated])
def osoba_update_delete(request, pk):
    try:
        osoba = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = OsobaSerializer(osoba, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)