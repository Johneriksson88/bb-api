from rest_framework import serializers
from .models import Contact

# contact serializer
class ContactSerializer(serializers.ModelSerializer):
    # custom serializer field setting the owner to the owners username
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Contact
        fields = [
            'id',
            'owner',
            'created_at',
            'updated_at',
            'title',
            'email',
            'message',
        ]