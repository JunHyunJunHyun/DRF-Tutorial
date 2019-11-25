from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework import viewsets

from . import models
from . import serializers
from . import permissions as custom_permissions


@api_view(("GET",))
def api_root(request, format=None):

    """
    그냥 API 시작 포인트에서 엔드 포인트들 설명해주는 역할인듯
    """

    return Response(
        {
            "users": reverse("user-list", request=request, format=format),
            "snippets": reverse("snippet-list", request=request, format=format),
        }
    )


class UserViewSet(viewsets.ReadOnlyModelViewSet):

    """
    이 뷰셋은 `list`와 `detail` 기능을 자동으로 지원합니다
    """

    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):

    """
    이 뷰셋은 `list`와 `create`, `retrieve`, `update`, 'destroy` 기능을 자동으로 지원합니다

    여기에 `highlight` 기능의 코드만 추가로 작성했습니다
    """

    queryset = models.Snippet.objects.all()
    serializer_class = serializers.SnippetSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custom_permissions.IsOwnerOrReadOnly,
    )

    @action(renderer_classes=[renderers.StaticHTMLRenderer], detail=True)
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

