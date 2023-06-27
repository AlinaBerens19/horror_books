from contextvars import Token
from django import views
from django.shortcuts import get_object_or_404
from requests import Response
from rest_framework import generics
from .models import User
from .serializers import LoginSerializer, RegisterSerializer, UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from . import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login
from django.contrib.auth import login, authenticate
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from . import serializers


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsOwnerOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer  


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 

    def get_object(self):
        email = self.kwargs['email']
        obj = get_object_or_404(User, email=email)
        self.check_object_permissions(self.request, obj)
        return obj
    

class UserLogin(APIView):
    
    def post(self, request, format=None):
        serializer = serializers.LoginSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        # Login the user
        login(request, user)

        token = get_tokens_for_user(user)

        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'phone': user.phone,
            'token': token,
            'profile_picture': user.profile_picture.url if user.profile_picture else ''
        }
        return Response({'user': user_data, 'message': 'User is authenticated'}, status=200)


class UserProfile(APIView):
    permission_classes = [permissions.IsOwnerOrReadOnly]

    def get(self, request, format=None):
        email = request.query_params.get('email')

        if not email:
            return Response({'error': 'Missing email parameter'}, status=400)

        try:
            user = User.objects.get(email=email)
            
        except User.DoesNotExist:
            print('EMAIL ==> ', email)
            return Response({'error': 'User not found'}, status=404)

        serializer = serializers.ProfileSerializer(user.profile)
        return Response(serializer.data)
    

    def put(self, request, format=None):
        email = request.query_params.get('email')

        if not email:
            return Response({'error': 'Missing email parameter'}, status=404)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)

        serializer = serializers.ProfileSerializer(user.profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=404)


    def delete(self, request, format=None):
        email = request.query_params.get('email')

        if not email:
            return Response({'error': 'Missing email parameter'}, status=404)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=404)

        user.profile.delete()
        user.delete()
        return Response(status=204)
    
