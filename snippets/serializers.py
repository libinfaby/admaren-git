from rest_framework import serializers

from .models import Snippet, Tag


# SNIPPET SERIALIZERS

class SnippetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = '__all__'


class SnippetOverviewSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name='snippet-detail',
        read_only=True,
    ) 

    update = serializers.HyperlinkedIdentityField(
        view_name='snippet-update',
        read_only=True,
    ) 

    delete = serializers.HyperlinkedIdentityField(
        view_name='snippet-delete',
        read_only=True,
    ) 

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'detail', 'update', 'delete']


class SnippetDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Snippet
        fields = ['title', 'content', 'timestamp']


# TAG SERIALIZERS

class TagSerializer(serializers.ModelSerializer):
    detail = serializers.HyperlinkedIdentityField(
        view_name='tag-detail',
        read_only=True,
    ) 

    class Meta:
        model = Tag
        fields = ['id', 'title', 'detail']
