from .models import Osoba
from .serializers import OsobaSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

osoba = Osoba(imie="Magda", nazwisko="Kowal", plec="Kobieta", stanowisko="Tynkarz", data_dodania="2023-11-04")
osoba.save()

serializer = OsobaSerializer(osoba)
serializer.data

content = JSONRenderer().render(serializer.data)
content

import io
stream = io.BytesIO(content)
data = JSONParser().parse(stream)

deserializer = OsobaSerializer(data=data)
deserializer.is_valid()

deserializer.save()
deserializer.data