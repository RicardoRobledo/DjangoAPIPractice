# from rest_framework import generics, permissions
from .models import Post
from rest_framework import viewsets # new
from django.contrib.auth import get_user_model # new
from .permissions import IsAuthorOrReadOnly # new
from .serializers import PostSerializer, UserSerializer # new
from django.contrib.auth import get_user_model # new


# Project-Level Permissions
#
# AllowAny - any user, authenticated or not, has full access
# IsAuthenticated - only authenticated, registered users have access
# IsAdminUser - only admins/superusers have access
# IsAuthenticatedOrReadOnly - unauthorized users can view any page, but only authenticated users have write, edit, or delete privileges

'''
class PostList(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,) # new
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,) # new
    permission_classes = (IsAuthorOrReadOnly,) # new
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserList(generics.ListCreateAPIView): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
'''


class PostViewSet(viewsets.ModelViewSet): # new
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
