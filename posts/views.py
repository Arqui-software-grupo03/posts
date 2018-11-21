from rest_framework import viewsets, generics

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

    def get_queryset(self):
        return Answer.objects.filter(post=self.kwargs['post'])

class UsersPostsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts from an specific user to be viewed ¿or edited?.
    """
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

    def get_queryset(self):
        return Posts.objects.filter(user_id=self.kwargs['author'])


# class AnswerList(generics.ListAPIView):
#     serializer_class = AnswerSerializer
#
#     def get_queryset(self):
#         """
#         This view should return a list of all the answers for
#         the post as determined by the post portion of the URL.
#         """
#         post_id = self.kwargs['post']
#         return Answer.objects.filter(post='https://localhost:8100/posts/{}'.format(post_id))
