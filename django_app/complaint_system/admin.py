from django.contrib import admin
from complaint_system.models import Complaint

class ComplaintAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Complaint Location',               {'fields': ['address']}),
        ('Complaint Category',               {'fields': ['category']}),
    ]

admin.site.register(Complaint, ComplaintAdmin)