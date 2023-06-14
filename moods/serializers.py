from rest_framework import serializers
from moods.models import Mood


class MoodSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    mood_id = serializers.ReadOnlyField(source='mood.id')
    posts = serializers.ReadOnlyField(source='posts.models.post.moods')

    print(f"posts {posts}")

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Mood
        fields = [
            'id', 'mood_id', 'owner', 'created_at', 'updated_at', 'name', 'emoji', 'posts'
        ]