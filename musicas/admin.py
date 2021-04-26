from django.contrib import admin
from .models import Musica, UserResps
# Register your models here.

class MusicaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'tipo', 'fase')

admin.site.register(Musica, MusicaAdmin)
admin.site.register(UserResps)