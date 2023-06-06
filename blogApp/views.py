from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from . models import *
from . serializers import *
# Create your views here.


class Helper():

    def getObject(self,model,slug):
        return get_object_or_404(model,slug = slug)

    def checkValid(self,serializer,flag=False):
        if serializer.is_valid():
            serializer.save()
            if not flag:
                return Response(serializer.data, status = status.HTTP_200_OK)
            else:
                return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)


class PostViewSet(viewsets.ViewSet,Helper):

    lookup_field = 'slug'

    def list(self,request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many = True)
        return Response(serializer.data)

    def retrieve(self, request, slug):
        serializer = PostSerializer(self.getObject(Post,slug), many = False)
        return Response(serializer.data)

    def create(self, request):
        serializer = PostSerializer(data = request.data)
        self.checkValid(serializer, flag=True)

    def update(self, request, slug):
        serializer = PostSerializer(self.getObject(Post,slug),data = request.data)
        self.checkValid(serializer)

    def destroy(self, request, slug):
        post =  self.getObject(Post,slug)
        post.delete()
        return Response(status = status.HTTP_200_OK)





class UserViewSet(viewsets.ViewSet, Helper):

    def list(self,request):
        queryset = UserAccount.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk):
        user_list = get_object_or_404(UserAccount, pk = pk)
        serializer = UserSerializer(user_list)
        return Response(serializer.data)

    def create(self, request):
        serializer = UserSerializer(data = request.data)
        self.checkValid(serializer, flag= True)

    def update(self, request, pk):

        user = get_object_or_404(UserAccount, pk = pk)
        serializer = UserSerializer(user, data = request.data)
        self.checkValid(serializer)

    def destroy(self, request, pk):

        user = get_object_or_404(UserAccount, pk = pk)
        user.delete()
        return Response(status = status.HTTP_200_OK)

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user: UserAccount):
        token = super().get_token(user)
        token['name'] = user.name
        token['email'] = user.email
        token['user_id'] = user.id
        return token

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CommentViewSet(APIView):

    def get(self,request,slug):
        slug = self.kwargs['slug']
        post = Post.objects.get(slug=slug)
        queryset = Comment.objects.filter(post=post)
        serializer = CommentSerializer(queryset, many = True)
        return Response(serializer.data)
    
    def post(self,request,slug):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    


class AddComment(APIView):
    def post(self,request,slug):
        serializer = CreateCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class GetLatestPost(APIView):

    def get(self,request):
        posts = Post.objects.all().order_by('-uploadedOn')[:3]
        serializer = PostSerializer(posts, many= True)
        return Response(serializer.data)

