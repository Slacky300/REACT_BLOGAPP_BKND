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