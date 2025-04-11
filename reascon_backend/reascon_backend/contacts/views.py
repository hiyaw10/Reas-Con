# contacts/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Contact, ProjectInquiry
from .serializers import ContactSerializer, ProjectInquirySerializer

class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"success": True, "message": "Thank you for your message!"},
            status=status.HTTP_201_CREATED
        )

class ProjectInquiryCreateView(generics.CreateAPIView):
    queryset = ProjectInquiry.objects.all()
    serializer_class = ProjectInquirySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"success": True, "message": "Thank you for your project inquiry!"},
            status=status.HTTP_201_CREATED
        )