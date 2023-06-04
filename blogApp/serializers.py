from django.urls import reverse
from . models import *
from rest_framework import serializers







class PostSerializer(serializers.ModelSerializer):

    noOfCmnts = serializers.SerializerMethodField('_noOfCmnts')

    def _noOfCmnts(self, obj):
        slug = getattr(obj, 'slug')
        post = Post.objects.get(slug = slug)
        cmnt = Comment.objects.filter(post = post).count()
        return cmnt

    class Meta:
        model = Post
        fields = ['id','title','category','img','desc','uploadedOn','slug','likes','file','noOfCmnts']
    
    


    


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['pk','email','name','password']


class CommentSerializer(serializers.ModelSerializer):

    byUser = UserSerializer()
    class Meta:
        model = Comment
        fields = ['pk','text','byUser','post','cmntDate','likes']
    

class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
    