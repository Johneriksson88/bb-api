from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from bb_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer

# comment list view
class CommentList(generics.ListCreateAPIView):
    # list comments or create a comment if logged in.
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# comment detail view
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    # retrieve a comment, or update or delete it by id if you own it.
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()