from django.contrib import admin
from Locadora.models import Fita, Locacao, Titulo

admin.site.register(Titulo)
admin.site.register(Fita)
admin.site.register(Locacao)
