from django.contrib.auth import get_user_model
from django.shortcuts import get_list_or_404, get_object_or_404, render
from .models import Review, Comment, Movie
from .serializers import CommentSerializer, ReviewSerializer, ReviewListSerializer
from movies.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import api_view

# GET일 때 전체 리뷰 불러오기, POST일때 리뷰 생성


@api_view(['POST', 'GET'])
def review_list_create(request):
    # 리뷰 전체 리스트 받아오기
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializers = ReviewListSerializer(reviews, many=True)
        return Response(serializers.data, status=status.HTTP_201_CREATED)

    if request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)
        print(request.data)
        movie = Movie.objects.get(title=request.data['movie']['title'])
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# 사용자가 고른 영화의 review 받아오기
@api_view(['GET'])
def review_list_get(request):
    if request.method == 'GET':
        movie_title = request.GET['movie_title']
        print(movie_title)
        movie = get_object_or_404(Movie, title=movie_title)
        reviews = Review.objects.filter(movie_id=movie.id)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


# GET일때 하나의 리뷰 디테일 정보 불러오기, PUT일때 업데이트, DELETE일때 삭제
@api_view(['GET', 'PUT', 'DELETE'])
def review_update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(instance=review, data=request.data)
        movie = Movie.objects.get(title=request.data['movie']['title'])
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        data = {
            'delete': f'{review_pk}번 리뷰가 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def comment_list_create(request, review_pk):
    if request.method == 'GET':
        comments = Comment.objects.filter(review_id=review_pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        review = Review.objects.get(id=review_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
  
       
@api_view(['DELETE', 'PUT'])
def comment_delete_update(request, review_pk, comment_pk):
    comment = Comment.objects.get(id = comment_pk)
    review = Review.objects.get(id=review_pk)
    if request.method == 'DELETE':
        comment.delete()
        return Response(status.HTTP_200_OK)

    if request.method == 'PUT':
        serializer = ReviewSerializer(instance=review, data=request.data)
        movie = Movie.objects.get(title=request.data['movie']['title'])
        if serializer.is_valid(raise_exception=True):
            serializer.save(movie=movie)
            return Response(serializer.data)
            
        return Response(status.HTTP_200_OK)


def like(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if review.like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
