from django.contrib import admin

from .models import Resident, Film, Character, Planet

admin.site.register(Resident)
admin.site.register(Film)
admin.site.register(Character)
admin.site.register(Planet)