from django.contrib import admin
from .models import Certificate, Resume, Education


class CertificateAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee']
    list_display_links = ['id', 'employee']
    search_fields = ['employee__name']


class ResumeAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee']
    list_display_links = ['id', 'employee']
    search_fields = ['employee__name']


class EducationAdmin(admin.ModelAdmin):
    list_display = ['id', 'employee', 'name', 'address']
    list_display_links = ['id', 'employee', 'name']
    search_fields = ['employee__name', 'name', 'address', 'description']


admin.site.register(Certificate, CertificateAdmin)
admin.site.register(Resume, ResumeAdmin)
admin.site.register(Education, EducationAdmin)