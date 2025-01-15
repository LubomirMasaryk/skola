from django.contrib import admin
from .models import *

admin.site.register(Kniha)
admin.site.register(Autor)
admin.site.register(Vydavatel)
admin.site.register(Miesto)