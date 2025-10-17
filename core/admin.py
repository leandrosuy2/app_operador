# core/admin.py
from django.contrib import admin
from .models import Anexo
@admin.register(Anexo)
class AnexoAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "arquivo", "uploaded_at", "size")
    search_fields = ("arquivo",)
