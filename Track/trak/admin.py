from django.contrib import admin
from trak.models import quest, Person, NowExp, Persons

# Register your models here.
admin.site.register(quest)
admin.site.register(Persons)
admin.site.register(Person)
admin.site.register(NowExp)