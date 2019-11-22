from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
from . import serializers


class SnippetList(APIView):

    """
    코드 조각을 모두 보여주거나 새 코드 조각을 만듭니다.
    """

    def get(self, request, format=None):
        snippets = models.Snippet.objects.all()
        serializer = serializers.SnippetSerializer(snippets, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.SnippetSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):

    """
    코드 조각 조회, 업데이트, 삭제
    """

    def get_object(self, pk):
        try:
            snippet = models.Snippet.objects.get(pk=pk)
        except models.Snippet.DoesNotExist:
            return Response(status=404)

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = serializers.SnippetSerializer(snippet)

        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = serializers.SnippetSerializer(snippet, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
