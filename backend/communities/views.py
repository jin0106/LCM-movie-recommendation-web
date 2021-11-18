from django.contrib.auth import get_user_model
from django.shortcuts import get_list_or_404, get_object_or_404, render
from .models import Review, Comment
from .serializers import CommentSerializer, ReviewSerializer, ReviewListSerializer
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import api_view

# GET일 때 전체 리뷰 불러오기, POST일때 리뷰 생성


@api_view(['GET', 'POST'])
def review_list_create(request):
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# GET일때 하나의 리뷰 디테일 정보 불러오기, PUT일때 업데이트, DELETE일때 삭제


@api_view(['GET', 'PUT', 'DELETE'])
def review_update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        data = {
            'delete': f'{review_pk}번 리뷰가 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def comment_list_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if request.method == 'GET':
        comments = Comment.objects.filter(review_id=review_pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        comment = Comment(content=request.data.get(
            'content'), review=review, user=User)
        comment.save()
        serializer = CommentSerializer(comment)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


def comment_delete_update(request, review_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        comment.delete()


def like(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    if review.like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
