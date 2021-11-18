from django.http import response
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserSerializer
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
    
    pass
    
        