from os import stat
from django.contrib.auth import get_user_model
from django.http import response
from django.shortcuts import get_list_or_404, render
from rest_framework import serializers, status
from rest_framework.response import Response
from config.settings import SECRET_KEY, ALGORITHM, PASSWORD
from movies.models import Genre
from .serializers import UserSerializer
from movies.serializers import GenreListSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import os
import sys
import urllib.request
import jwt
import requests
import json
import datetime
# Create your views here.


@api_view(['GET','POST', 'DELETE'])
@permission_classes([AllowAny])
def signup(request):
    # 회원 가입 

    if request.method == 'POST':
        if request.data.get('password') != request.data.get('passwordconfirm'):
            return Response({'error': '비밀번호 확인해주세요.'}, status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            user.set_password(request.data.get('password'))
            user.save()
            return Response(serializer.data, status.HTTP_201_CREATED)

    # 회원 탈퇴
    elif request.method == 'DELETE':
        user = get_user_model().objects.get(id=request.user.id)
        user.delete()
        return Response(status.HTTP_200_OK)



@api_view(['GET'])
def getuserinfo(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT', 'DELETE'])
def updateuserinfo(request):
    serializer = UserSerializer(request.user, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def likegenre(request):
    if request.method == 'GET':
        genres = request.user.genre.all()
        serializer = GenreListSerializer(genres, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


@api_view(['POST'])
def google(request):
    id = request.data['id']
    
    if get_user_model().objects.filter(username=id).exists():
        user = get_user_model().objects.get(username = id)
        data = {
            "username" : user.username
        }
        return Response(data, status.HTTP_200_OK)
    else:
        get_user_model()(
            username = id,
            nickname = id,
        ).save()
        user = get_user_model().objects.get(username = id)
        user.set_password(PASSWORD)
        user.save()
        data = {
            "username" : user.username
        }
        
        return Response(data, status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def get_naver_info(request):
    token = request.data['token']
    header = "Bearer " + token # Bearer 다음에 공백 추가
    url = "https://openapi.naver.com/v1/nid/me"
    request = urllib.request.Request(url)
    request.add_header("Authorization", header)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):

        response_body = response.read()
        res_data = json.loads(response_body.decode('UTF-8'))
        id = res_data['response']['id']
        nickname = res_data['response']['nickname']

        # 응답 성공했을 때 유저 있는 지 확인, 있다면 기존 아이디를 돌려줌
        if get_user_model().objects.filter(username=id).exists():
            user = get_user_model().objects.get(username = id)
            data = {
            "username" : user.username
            }
            return Response(data, status.HTTP_200_OK)
        # 없다면 회원가입 시킨 후 돌려줌 
        else: 
            get_user_model()(
            username = id,
            nickname = nickname,
            ).save()
            user = get_user_model().objects.get(username = id)
            user.set_password(PASSWORD)
            user.save()
            data = {
                "username" : user.username
            }
            return Response(data, status.HTTP_200_OK)
    else:
        print("Error Code:" + rescode)
        return Response(status.HTTP_400_BAD_REQUEST)
    