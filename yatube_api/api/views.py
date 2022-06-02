from rest_framework import viewsets, filters, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet

from api.permissions import OnlyAuthorChangeObject
from api.serializers import (
    PostSerializer, GroupSerializer, CommentSerializer, FollowSerializer
)
from posts.models import Post, Group


class ListCreateViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    pass


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [OnlyAuthorChangeObject, IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (OnlyAuthorChangeObject,)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post_obj = get_object_or_404(Post, id=post_id)
        post_comments = post_obj.comments.all()
        return post_comments

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post_obj = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=post_obj)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AllowAny,)


class FollowViewSet(ListCreateViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
