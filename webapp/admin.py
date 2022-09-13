from django.contrib import admin
from .models import * 

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'subject',
        'message',
        'date_created'
    )
    
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'message',
        'date',
        'time',
        'date_created'
    )    

admin.site.register(Contact, ContactAdmin)
admin.site.register(Appointment, AppointmentAdmin)
