from django.contrib import admin
from .models import *
from django.utils.html import format_html 
# Register your models here.

# admin customization for Team
class TeamAdmin(admin.ModelAdmin):
    # display image in team admin section
    def myphoto(self, object):
        return format_html('<img src="{}" width="40"/>'.format(object.photo.url))

    # remember all paramters of this class is having list only
    list_display = ('id', 'myphoto', 'first_name', 'role', 'created_date')
    list_display_links = ('id', 'first_name')
    search_fields = ('first_name', 'role')
    list_filter = ('role', )

admin.site.register(Slider)
admin.site.register(Team, TeamAdmin)
