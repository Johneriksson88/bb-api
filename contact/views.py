from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.permissions import IsAdminUser

# contact list view
class ContactList(generics.ListCreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Contact.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# contact messages are not shown on the front end so they don't need a detail view
