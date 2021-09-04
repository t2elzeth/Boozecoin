from django.contrib import admin
from solo.admin import SingletonModelAdmin

from . import models


@admin.register(models.PagesContent)
class PagesAdmin(SingletonModelAdmin):
    pass
