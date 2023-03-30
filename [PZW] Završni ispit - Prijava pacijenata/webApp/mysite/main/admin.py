from django.contrib import admin
from .models import *

model_list = [Odjel, Pacijent]
admin.site.register(model_list)