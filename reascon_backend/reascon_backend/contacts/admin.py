# contacts/admin.py
from django.contrib import admin
from .models import Contact, ProjectInquiry

@admin.register(ProjectInquiry)
class ProjectInquiryAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'email', 'submitted_at')
    search_fields = ( 'name', 'email', 'message')
