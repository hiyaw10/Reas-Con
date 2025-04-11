# contacts/serializers.py
from rest_framework import serializers
from .models import Contact, ProjectInquiry

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'
        read_only_fields = ('submitted_at',)

class ProjectInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectInquiry
        fields = '__all__'
        read_only_fields = ('submitted_at',)