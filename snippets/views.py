from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from . import models
from . import serializers


@api_view(["GET", "POST"])
def snippet_list(request, format=None):

    """
    코드 조각을 모두 보여주거나 새 코드 조각을 만듭니다.
    """

    if request.method == "GET":
        snippets = models.Snippet.objects.all()
        serializer = serializers.SnippetSerializer(snippets, many=True)

        return Response(serializer.data)

    elif request.method == "POST":
        serializer = serializers.SnippetSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def snippet_detail(request, pk, format=None):

    """
    코드 조각 조회, 업데이트, 삭제
    """

    try:
        snippet = models.Snippet.objects.get(pk=pk)
    except models.Snippet.DoesNotExist:
        return Response(status=404)

    if request.method == "GET":
        serializer = serializers.SnippetSerializer(snippet)

        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = serializers.SnippetSerializer(snippet, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        snippet.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
