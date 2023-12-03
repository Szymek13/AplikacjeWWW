from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from ..models import Osoba, Stanowisko
from ..views import *

class OsobaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Osoba.objects.create(imie='Jan', nazwisko='Kowal', plec=1)

    def test_first_name_label(self):
        osoba = Osoba.objects.get(id=1)
        field_label = osoba._meta.get_field('imie').verbose_name
        self.assertEqual(field_label, 'imie')

    def test_first_name_max_length(self):
        osoba = Osoba.objects.get(id=1)
        max_length = osoba._meta.get_field('imie').max_length
        self.assertEqual(max_length, 60)

class StanowiskoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Stanowisko.objects.create(nazwa='Rolnik', opis='Nawozi pole')

    def test_name_max_length(self):
        stanowisko = Stanowisko.objects.get(id=1)
        max_length = stanowisko._meta.get_field('nazwa').max_length
        self.assertEqual(max_length, 100)

class OsobaDetailTest(TestCase):
    def setUp(self) -> None:
        self.user - User.objects.create_user(username='testuser', password='pass123')
        self.robert = Osoba.objects.create(imie='Robert', nazwisko='Rybak')

    def test_get_person_detail(self):
        factory = APIRequestFactory()
        request = factory.get(f'/mirex/osoby/{self.robert.pk}')

        force_authenticate(request, user=self.user)
        response = osoba_detail(request, self.robert.pk)
        serializer = OsobaSerializer(self.robert)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)