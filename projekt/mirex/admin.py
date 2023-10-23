from django.contrib import admin

# Register your models here.

from .models import Team
from .models import Person
from .models import Osoba
from .models import Stanowisko

class OsobaAdmin(admin.ModelAdmin):
    readonly_fields = ("data_dodania",)
    list_display = ['imie', 'nazwisko', 'stanowisko_display', 'data_dodania']
    list_filter = ('stanowisko', 'data_dodania')

    def stanowisko_display(self, obj):
        return f'{obj.stanowisko} ({obj.stanowisko_id})'
    stanowisko_display.short_description = 'Stanowisko'


admin.site.register(Team)
admin.site.register(Person)
admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Stanowisko)
