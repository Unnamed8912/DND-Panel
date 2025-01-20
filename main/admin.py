from django.contrib import admin

from main.models import character

@admin.register(character)
class characterAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}