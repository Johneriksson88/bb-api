from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Contact
        fields = '__all__'