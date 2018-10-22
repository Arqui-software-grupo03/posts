# from django.contrib.auth.models import User, Group
from rest_framework import viewsets
# from posts.serializers import UserSerializer, GroupSerializer

# from rest_framework import generics
from .models import Posts, Hashtag, Answer
from posts.serializers import PostsSerializer, HashtagSerializer, AnswerSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

class HashtagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hastags to be viewed or edited.
    """
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows answers to be viewed or edited.
    """
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
