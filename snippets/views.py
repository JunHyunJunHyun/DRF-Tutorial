from django.http import Http404
from rest_framework import mixins, generics

from . import models
from . import serializers


class SnippetList(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):

    """
    코드 조각을 모두 보여주거나 새 코드 조각을 만듭니다.
    """

    queryset = models.Snippet.objects.all()
    serializer_class = serializers.SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SnippetDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):

    """
    코드 조각 조회, 업데이트, 삭제
    """

    queryset = models.Snippet.objects.all()
    serializer_class = serializers.SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, format=None):
        return self.destroy(request, *args, **kwargs)
