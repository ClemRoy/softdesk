from rest_framework import serializers
from django.contrib.auth import get_user_model
from softdesk.models import Project,Contributor,Issue,Comment
from authentication.models import User


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'type', 'contributors']


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)

        return user

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'password']


class ContributorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contributor
        fields = ['id','user','project','role']
        read_only_fields = [ 'project' ]

class IssueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issue
        fields = ['id','title','description','tag','priority','project','status','assigned_user']
        read_only_fields= ['project','author']

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ['id','author','description']
        read_only_fields = ['issue','author']