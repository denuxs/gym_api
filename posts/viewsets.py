from rest_framework import viewsets

from posts.models import Post
from posts.serializers import PostSerializer
from django_filters.rest_framework import DjangoFilterBackend


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "user",
    ]
