from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Mood
from .serializers import MoodSerializer
from bb_api.permissions import IsOwnerOrReadOnly


class MoodList(APIView):
    serializer_class = MoodSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        moods = Mood.objects.all()
        serializer = MoodSerializer(
            moods, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = MoodSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class MoodDetail(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = MoodSerializer

    def get_object(self, pk):
        try:
            mood = Mood.objects.get(pk=pk)
            self.check_object_permissions(self.request, mood)
            return mood
        except Mood.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(
            post, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        mood = self.get_object(pk)
        serializer = PostSerializer(
            mood, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        mood = self.get_object(pk)
        mood.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )