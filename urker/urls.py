from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include, reverse_lazy
from .views import logout_view
from employees.views import EmployeeListView

admin.site.site_url = reverse_lazy('employees')
admin.site.site_header = 'Urker admin'
admin.site.site_title = 'Urker admin'
admin.site.index_title = 'Urker administration'
admin.empty_value_display = '**Empty**'
admin.site.logout = logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employees.urls')),
    path('logout/', logout_view, name='logout')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
