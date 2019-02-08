from rest_framework import generics
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


class SnippetList(generics.ListCreateAPIView):
    """
    - 全ての snippets を表示する。
    - 新しい snippet を作成する
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    単一のスニペットの、取得・更新・削除を行う。
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
