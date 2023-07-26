from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.permissions import IsAdminUser


class ContactList(generics.ListCreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Contact.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


