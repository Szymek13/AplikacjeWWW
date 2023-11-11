from mirex.models import Osoba
from mirex.models import Stanowisko
from mirex.serializers import OsobaSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import io

osoba = Osoba(imie="duck33", nazwisko="Smith", plec=1, stanowisko=Stanowisko.objects.get(nazwa="Tynkarz"), data_dodania="2023-11-06")
osoba.save()

serializer = OsobaSerializer(osoba)
serializer.data

content = JSONRenderer().render(serializer.data)
content

stream = io.BytesIO(content)
data = JSONParser().parse(stream)

deserializer = OsobaSerializer(data=data)
deserializer.is_valid()

deserializer.save()
deserializer.data