# contacts/admin.py
from django.contrib import admin
from .models import Contact, ProjectInquiry

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact_type', 'submitted_at')
    list_filter = ('contact_type',)
    search_fields = ('name', 'email', 'subject', 'message')

@admin.register(ProjectInquiry)
class ProjectInquiryAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'email', 'submitted_at')
    search_fields = ( 'name', 'email', 'message')