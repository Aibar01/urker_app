from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='employees'),
    path('<int:pk>/', views.EmployeeDetailView.as_view(), name='employee'),
    path('search/', views.SearchEmployeeListView.as_view(), name='search')
]