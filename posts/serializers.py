# from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Posts, Hashtag


class HashtagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hashtag
        fields = ("url", "name")

class PostsSerializer(serializers.HyperlinkedModelSerializer):
    hashtags = HashtagSerializer(many=True)

    class Meta:
        model = Posts
        fields = ("content", "hashtags")

    def create(self, validated_data):
        content = validated_data['content'].split(' ')
        tags = []
        for term in content:
            if term[0] == '#':
                tags.append(Hashtag.objects.create(name=term[1:]))

        post = Posts.objects.create(
            # url = validated_data['url'],
            content = validated_data['content'],
        )
        post.hashtags.set(tags)

        return post

# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')
