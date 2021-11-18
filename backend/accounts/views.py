from django.contrib.auth import get_user_model
from django.http import response
from django.shortcuts import get_list_or_404, render
from rest_framework import serializers, status
from rest_framework.response import Response

from movies.models import Genre
from .serializers import UserSerializer
from movies.serializers import GenreListSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    if request.data.get('password') != request.data.get('passwordconfirm'):
        return Response({ 'error': '비밀번호 확인해주세요.' }, status.HTTP_400_BAD_REQUEST)
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

@api_view(['GET'])
def likegenre(request):
    if request.method == 'GET':
        #user = request.user.id
        #genres = get_list_or_404(get_user_model(), name=user.genre)
        #serializer = GenreListSerializer(genres, many=True)
        #print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        # print(genres)
        return Response( status.HTTP_200_OK)
    
        