from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins, filters
from rest_framework.permissions import IsAuthenticated

from api.permissions import IsOwnerOrReadOnly
from api.serializers import (
    CommentSerializer,
    GroupSerializer,
    PostSerializer,
    FollowSerializer
)
from posts.models import Group, Post, Comment, Follow


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet для просмотра и редактирования постов."""

    queryset = Post.objects.all().select_related('author')
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        """
        Вызывается CreateModelMixin при
        сохранении нового экземпляра объекта.
        """
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet для просмотра и редактирования комментариев."""

    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get_post(self):
        """
        Вызывает модель Post и получает из нее объект,
        если этот объект или модель не существует, возникает ошибка 404.
        """
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        """
        Возвращает набор запросов, который следует
        использовать для просмотра списка постов
        """
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        """
        Вызывается CreateModelMixin при
        сохранении нового экземпляра объекта.
        """
        serializer.save(author=self.request.user, post=self.get_post())


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для просмотра групп."""

    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)


class FollowViewSet(viewsets.ModelViewSet):
    """ViewSet для просмотра подписок."""

    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
