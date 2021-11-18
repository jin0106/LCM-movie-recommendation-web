from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
app_name = "accounts"
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('likegenre/', views.likegenre, name='likegenre'),
    path('getuserinfo/', views.getuserinfo, name='getuserinfo'),
    path('updateuserinfo/', views.updateuserinfo, name='updateuserinfo'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]