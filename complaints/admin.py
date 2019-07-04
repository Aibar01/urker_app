from django.contrib import admin
from .models import Complaint


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee', 'reason'[:15], 'status']
    list_display_links = ['id', 'employee']
    search_fields = ['employee__name', 'reason', 'employee__surname', 'employee__id']
    list_filter = ['status']


admin.site.register(Complaint, ComplaintAdmin)