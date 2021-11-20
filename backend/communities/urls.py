from django.urls import path
from . import views

app_name = "communities"
urlpatterns = [
    path('', views.review_list_create),
    path('review/', views.review_list_get,),
    path('<int:review_pk>/', views.review_update_delete,),
    path('<int:review_pk>/comments/', views.comment_list_create),
    path('<int:review_pk>/comments/<int:comment_pk>/',
         views.comment_delete_update),
    path('<int:review_pk>/like/', views.like, name='like'),
]
