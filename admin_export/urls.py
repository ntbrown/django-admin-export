from django.urls import path, re_path
from django.contrib.admin.views.decorators import staff_member_required
from .views import AdminExport

view = staff_member_required(AdminExport.as_view())
urlpatterns = [
   path('export/', view, name="export"),
   path('export_to_xls/', view),  # compatibility for users who upgrade without touching URLs
]
