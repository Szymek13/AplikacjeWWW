Lab 3 (Zadanie 10)

<span style="color:gray">py manage.py shell</span>

<span style="color:gray">from mirex.models import Osoba, Stanowisko</span>

Wyświetl wszystkie obiekty modelu Osoba:

<span style="color:gray">Osoba.objects.all()</span>

Wyświetl obiekt modelu Osoba z id=3:

<span style="color:gray">Osoba.objects.get(pk=3)</span>

Wyświetl obiekty modelu Osoba, których nazwa rozpoczyna się na wybraną przez Ciebie literę alfabetu (tak, żeby był co najmniej jeden wynik):

<span style="color:gray">Osoba.objects.filter(nazwisko__startswith='R')</span>

Wyświetl unikalną listę stanowisk przypisanych dla modeli Osoba:

<span style="color:gray">Osoba.objects.values_list('stanowisko').distinct()</span>

Wyświetl nazwy stanowisk posortowane alfabetycznie malejąco:

<span style="color:gray">Osoba.objects.values_list('-stanowisko__nazwa', flat=True).distinct().order_by('stanowisko__nazwa')</span>

Dodaj nową instancję obiektu klasy Osoba i zapisz w bazie:

<span style="color:gray">new_stanowisko = Stanowisko.objects.get(id=2)</span>

<span style="color:gray">new_osoba = Osoba(plec=1, imie="Dawid", nazwisko="Kowalski", stanowisko=new_stanowisko)</span>

<span style="color:gray">new_osoba.save()</span>
