# contacts/models.py
from django.db import models

class Contact(models.Model):
    CONTACT_TYPE_CHOICES = [
        ('quote', 'Request a Quote'),
        ('general', 'General Inquiry'),
    ]

    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)  # CharField instead of EmailField
    phone = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    contact_type = models.CharField(
        max_length=10,
        choices=CONTACT_TYPE_CHOICES,
        default='general'
    )
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.contact_type}"

class ProjectInquiry(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry for Project {self.project_id} by {self.name}"