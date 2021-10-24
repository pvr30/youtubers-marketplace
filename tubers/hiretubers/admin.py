from django.contrib import admin
from .models import Hiretuber, Contact
# Register your models here.

class HireTuberAdmin(admin.ModelAdmin):
    list_display = ('email', 'tuber_name', 'state')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject', 'company_name')

admin.site.register(Hiretuber, HireTuberAdmin)
admin.site.register(Contact, ContactAdmin)

