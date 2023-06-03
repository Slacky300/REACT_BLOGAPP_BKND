from django.urls import reverse
from . models import *
from rest_framework import serializers







class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['pk','email','name','password']


class CommentSerializer(serializers.ModelSerializer):

    
    class Meta:
        model = Comment
        fields = '__all__'