from django.contrib.auth.models import User
from rest_framework import generics, permissions

from . import models
from . import serializers
from . import permissions as custom_permissions


class SnippetList(generics.ListCreateAPIView):

    """
    코드 조각을 모두 보여주거나 새 코드 조각을 만듭니다.
    """

    queryset = models.Snippet.objects.all()
    serializer_class = serializers.SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):

    """
    코드 조각 조회, 업데이트, 삭제
    """

    queryset = models.Snippet.objects.all()
    serializer_class = serializers.SnippetSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custom_permissions.IsOwnerOrReadOnly,
    )


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
