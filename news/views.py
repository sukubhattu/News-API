from rest_framework import generics
from .models import News
from .serializers import NewsSerializers

# Custom permission
from .permissions import IsAuthorOrReadOnly


class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = News.objects.all()
    serializer_class = NewsSerializers
