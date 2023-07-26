from rest_framework.views import APIView
from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.permissions import IsAdminUser
from bb_api.permissions import IsOwnerOrReadOnly


class ContactList(APIView):
    serializer_class = ContactSerializer
    permission_classes = (IsAdminUser,)
    queryset = Contact.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

