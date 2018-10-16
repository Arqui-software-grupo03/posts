# from django.contrib.auth.models import User, Group
# from posts.serializers import UserSerializer, GroupSerializer
from rest_framework import viewsets, response

# from rest_framework import generics
from .models import Posts, Hashtag
from posts.serializers import PostsSerializer, HashtagSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows posts to be viewed or edited.
    """
    queryset = Posts.objects.all()
    lookup_field = 'id'
    serializer_class = PostsSerializer

#necesario?
class HashtagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows hastags to be viewed or edited.
    """
    queryset = Hashtag.objects.all()
    serializer_class = HashtagSerializer


# class ListPostsView(generics.ListAPIView):
#     """
#     Provides a get method handler
#     """
#     queryset = Posts.objects.all()
#     serializer_class = PostsSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
