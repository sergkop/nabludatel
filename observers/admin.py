from django.contrib import admin

from observers.models import Observer

class ObserverAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'telephone', 'in_moscow', 'location', 'email')
    ordering = ('full_name',)
    search_fields = ('full_name',)

admin.site.register(Observer, ObserverAdmin)
