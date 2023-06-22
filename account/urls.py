from . import views
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user-list'),
    path('login/', views.UserLogin.as_view(), name='user-login'),
    path('register/', views.RegisterView.as_view(), name='user-login'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
