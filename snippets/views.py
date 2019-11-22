from rest_framework import generics

from . import models
from . import serializers


class SnippetList(generics.ListCreateAPIView):

    """
    코드 조각을 모두 보여주거나 새 코드 조각을 만듭니다.
    """

    queryset = models.Snippet.objects.all()
    serializer_class = serializers.SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):

    """
    코드 조각 조회, 업데이트, 삭제
    """

    queryset = models.Snippet.objects.all()
    serializer_class = serializers.SnippetSerializer
