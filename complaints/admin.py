from django.contrib import admin
from complaints.models import Complaint, Building


class ComplaintAdmin(admin.ModelAdmin):
    fieldsets = [
        #('Complaint Location', {'fields': ['address']}),
        #('Complaint Category', {'fields': ['category']}),
    ]


class BuildingAdmin(admin.ModelAdmin):
    fieldsets = [
        #('Complaint Location', {'fields': ['address']}),
        #('Complaint Category', {'fields': ['category']}),
    ]

admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Building, BuildingAdmin)
