# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Posts

from datetime import datetime


class PostsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Posts
        fields = ("id","content","pub_date")

    def create(self, validated_data):
        post = Posts.objects.create(content=validated_data['content'],
                                    pub_date=datetime.now())
        return post


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')
