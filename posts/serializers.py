# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Posts, Hashtag
from django.core.exceptions import ObjectDoesNotExist

from datetime import datetime


class HashtagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hashtag
        fields = ("id", "name", "posts_set")

class PostsSerializer(serializers.HyperlinkedModelSerializer):
    hashtags = HashtagSerializer(required=False, many=True)

    class Meta:
        model = Posts
        fields = ("id","content","pub_date", "hashtags")

    def create(self, validated_data):
        content = validated_data['content'].split(' ')
        tags = []
        for term in content:
            if '#' in term:
                i = term.find('#')
                try:
                    tag = Hashtag.objects.get(name=term[i+1:])
                except ObjectDoesNotExist as err:
                    tag = Hashtag.objects.create(name=term[i+1:])
                tags.append(tag)
        post = Posts.objects.create(content=validated_data['content'],
                                    pub_date=datetime.now())
        # post.hashtags.set(tags)
        if len(tags) > 0:
            post.hashtags.add(*tags)
        for t in tags:
            t.posts_set.add(post)
        return post


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')
