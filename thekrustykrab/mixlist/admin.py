from django.contrib import admin
from .models import Mix, Track, ExternalLink, Profile

# Register your models here.
admin.site.register(Mix)
admin.site.register(Track)
admin.site.register(ExternalLink)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'location')