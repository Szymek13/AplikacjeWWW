from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.

# deklaracja statycznej listy wyboru do wykorzystania w klasie modelu
MONTHS = models.IntegerChoices('Miesiace', 'Styczeń Luty Marzec Kwiecień Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień')

SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

PLEC = (
    ('M', 'Mężczyzna'),
    ('K', 'Kobieta')
)


class Team(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}"


class Person(models.Model):

    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default=SHIRT_SIZES[0][0])
    month_added = models.IntegerField(choices=MONTHS.choices, default=MONTHS.choices[0][0])
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=100)
    opis = models.CharField(max_length=300)
    def __str__(self):
        return self.nazwa

class Osoba(models.Model):
    class Plec(models.IntegerChoices):
        MEZCZYZNA = 1
        KOBIETA = 2

    imie = models.CharField(max_length=60)
    nazwisko = models.CharField(max_length=100)
    plec = models.IntegerField(choices=Plec.choices) #default=Plec.choices[0]
    stanowisko = models.ForeignKey(Stanowisko, null=True, blank=True, on_delete=models.SET_NULL)
    data_dodania = models.DateField(default=timezone.now())

    class Meta:
        ordering = ["nazwisko"]
    def __str__(self):
        return f'{self.imie} {self.nazwisko}'




