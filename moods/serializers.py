from rest_framework import serializers
from moods.models import Mood


class MoodSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    mood_id = serializers.ReadOnlyField(source='mood.id')
    name = serializers.ReadOnlyField(source='owner.mood.name')
    posts = serializers.ReadOnlyField(source='owner.mood.posts')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Mood
        fields = [
            'id', 'mood_id', 'owner', 'created_at', 'updated_at', 'name', 'emoji', 'posts'
        ]