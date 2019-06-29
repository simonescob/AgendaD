# Django Contact Admin

from django.contrib import admin
from .models import Contact

# admin.site.register(Contact)

class ContactAdmin(admin.ModelAdmin):
  list_display = ('user', 'first_name', 'last_name', 'number')

admin.site.register(Contact, ContactAdmin)